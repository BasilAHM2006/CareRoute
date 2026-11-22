"""Read-only deployment smoke checks for the current CareRoute data and API."""
from __future__ import annotations

import json
import os
import sys
import threading
import urllib.error
import urllib.request
from http.server import ThreadingHTTPServer
from pathlib import Path
from email.message import Message

ROOT = Path(__file__).resolve().parents[1]
os.environ["CAREROUTE_PREBUILT_INDEX"] = "1"
os.environ["CAREROUTE_INDEX_PATH"] = str(ROOT / "frontend/.data/facility_search.sqlite3")
os.environ["CAREROUTE_EXPECTED_FACILITY_COUNT"] = "166462"
os.environ["CAREROUTE_ALLOWED_ORIGINS"] = "https://careroute-web.onrender.com"
sys.path.insert(0, str(ROOT / "frontend/server"))

import search_api as api  # noqa: E402


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)
    print(f"PASS {message}")


def request(base: str, path: str, origin: str | None = None):
    headers = {"Origin": origin} if origin else {}
    with urllib.request.urlopen(urllib.request.Request(f"{base}{path}", headers=headers), timeout=8) as response:
        return response.status, response.headers, response.read()


def main() -> None:
    count = api.validate_index()
    require(count == 166462, "prebuilt SQLite integrity, schema, FTS and 166,462 record count")
    require(api.validate_runtime_data() == (4, 16, 1000), "startup validation preserves pilot/provider and isolated demo source counts")

    import pandas as pd
    import pyarrow.parquet as parquet

    raw_count = parquet.ParquetFile(ROOT / "data/raw/india_public_healthcare.parquet").metadata.num_rows
    clean_parquet = ROOT / "data/processed/india_healthcare_cleaned.parquet"
    cleaned_ids = pd.read_parquet(clean_parquet, columns=["entity_uid"], engine="pyarrow")["entity_uid"].astype(str).tolist()
    csv_ids = pd.read_csv(ROOT / "data/processed/india_healthcare_cleaned.csv", usecols=["entity_uid"], dtype=str, keep_default_na=False)["entity_uid"].tolist()
    require(raw_count == count == len(cleaned_ids) == len(csv_ids), "raw, cleaned Parquet, cleaned CSV, and index row counts agree")
    require(cleaned_ids == csv_ids, "cleaned CSV and Parquet entity_uid order remains aligned")

    options = api.facility_options({"state": "Tamil Nadu"})
    require("Tamil Nadu" in options["states"] and bool(options["districts"]), "facility options retain state and district search values")

    public_page = api.query_facilities({"q": "", "state": "Tamil Nadu", "page": "1", "page_size": "2"})
    require(public_page["total"] > 0 and len(public_page["items"]) == 2, "public facility filtering and pagination")
    require(bool(public_page["items"][0]["entity_uid"]), "public results preserve entity_uid")

    providers = api.query_pilot({"q": "Nagercoil"})
    offer_count = sum(len(provider["offers"]) for provider in providers)
    require(len(providers) == 4 and offer_count == 16, "four Nagercoil organizations retain all 16 service offers")
    for service in ("nursing", "physiotherapy"):
        home = api.query_pilot({"q": "Nagercoil", "service": service, "home_only": "true"})
        require(len(home) == 1 and home[0]["provider_name"].casefold() == "calwin hospitals", f"{service} home-visit filtering is limited to Calwin")

    demos = api.query_demo({"page": "1", "page_size": "50"})
    require(demos["total"] == 1000 and len(demos["items"]) == 50, "all 1,000 synthetic records remain separately paginated")
    require(all(row.get("record_type") == "SYNTHETIC_DEMO_ONLY" for row in demos["items"]), "demo endpoint returns only explicitly synthetic records")

    published = ROOT / "frontend/dist"
    forbidden = {".parquet", ".csv", ".sqlite", ".db"}
    require(published.is_dir() and not any(path.suffix.casefold() in forbidden for path in published.rglob("*")), "frontend publish directory contains no datasets or SQLite index")

    handler = object.__new__(api.Handler)
    handler.headers = Message()
    handler.headers["Origin"] = "https://careroute-web.onrender.com"
    require(handler.origin_is_allowed(), "configured production frontend origin passes CORS allowlist")
    handler.headers = Message()
    handler.headers["Origin"] = "https://untrusted.example"
    require(not handler.origin_is_allowed(), "unlisted browser origin fails CORS allowlist")

    server = None
    try:
        server = ThreadingHTTPServer(("127.0.0.1", 0), api.Handler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        base = f"http://127.0.0.1:{server.server_port}"

        status, headers, body = request(base, "/api/health", "https://careroute-web.onrender.com")
        health = json.loads(body)
        require(status == 200 and headers.get("Access-Control-Allow-Origin") == "https://careroute-web.onrender.com", "health endpoint and allowlisted production CORS")
        require(health == {"status": "ok", "facility_count": 166462, "pilot_provider_count": 4, "synthetic_demo_count": 1000}, "health reports expected facility, provider, and demo counts")

        status, _, body = request(base, "/api/facilities?state=Tamil%20Nadu&page=1&page_size=1")
        require(status == 200 and json.loads(body)["total"] > 0, "HTTP public facility search endpoint")
        status, _, body = request(base, "/api/pilot?q=Nagercoil")
        require(status == 200 and len(json.loads(body)) == 4, "HTTP Nagercoil provider endpoint")
        status, _, body = request(base, "/api/demo?page=1&page_size=1000")
        require(status == 200 and json.loads(body)["total"] == 1000, "HTTP isolated demo endpoint")

        try:
            request(base, "/api/health", "https://untrusted.example")
            raise AssertionError("untrusted CORS origin unexpectedly succeeded")
        except urllib.error.HTTPError as exc:
            require(exc.code == 403, "untrusted browser origins are rejected")
    except OSError as exc:
        print(f"SKIP local HTTP integration checks: this environment cannot bind loopback sockets ({exc})")
    finally:
        if server:
            server.shutdown()
            server.server_close()


if __name__ == "__main__":
    main()
