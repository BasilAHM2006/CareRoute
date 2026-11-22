FROM python:3.12-slim AS index-builder

ENV PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    CAREROUTE_INDEX_PATH=/app/build/facility_search.sqlite3
WORKDIR /app

COPY requirements-deploy.txt ./requirements-deploy.txt
RUN python -m pip install --no-cache-dir -r requirements-deploy.txt

# Only the source files required for index generation and API operation enter
# the image build context. Raw inputs are validated during this build stage.
COPY frontend/server/search_api.py ./frontend/server/search_api.py
COPY data/raw/india_public_healthcare.parquet ./data/raw/india_public_healthcare.parquet
COPY data/raw/careroute_1000_clean_synthetic_demo_records.csv ./data/raw/careroute_1000_clean_synthetic_demo_records.csv
COPY data/processed/india_healthcare_cleaned.parquet ./data/processed/india_healthcare_cleaned.parquet
COPY data/processed/india_healthcare_cleaned.csv ./data/processed/india_healthcare_cleaned.csv
COPY data/processed/nagercoil_verified_provider_pilot.csv ./data/processed/nagercoil_verified_provider_pilot.csv
RUN python frontend/server/search_api.py --build-index-only \
    && python frontend/server/search_api.py --validate-index-only \
    && python frontend/server/search_api.py --validate-runtime-data-only

FROM python:3.12-slim AS runtime
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    CAREROUTE_PREBUILT_INDEX=1 \
    CAREROUTE_INDEX_PATH=/app/index/facility_search.sqlite3 \
    CAREROUTE_EXPECTED_FACILITY_COUNT=166462 \
    CAREROUTE_EXPECTED_PILOT_PROVIDERS=4 \
    CAREROUTE_EXPECTED_PILOT_OFFERS=16 \
    CAREROUTE_EXPECTED_DEMO_COUNT=1000 \
    CAREROUTE_API_HOST=0.0.0.0
WORKDIR /app
RUN groupadd --system --gid 10001 careroute \
    && useradd --system --uid 10001 --gid careroute --home-dir /nonexistent careroute \
    && mkdir -p /app/index /app/data/processed /app/data/raw \
    && chown -R careroute:careroute /app

# Runtime contains only the API, derived search index, four-provider pilot
# source, and isolated synthetic demo source. Public source datasets are never
# copied into the frontend's published static directory.
COPY --from=index-builder --chown=careroute:careroute /app/frontend/server/search_api.py ./frontend/server/search_api.py
COPY --from=index-builder --chown=careroute:careroute /app/build/facility_search.sqlite3 ./index/facility_search.sqlite3
COPY --from=index-builder --chown=careroute:careroute /app/data/processed/nagercoil_verified_provider_pilot.csv ./data/processed/nagercoil_verified_provider_pilot.csv
COPY --from=index-builder --chown=careroute:careroute /app/data/raw/careroute_1000_clean_synthetic_demo_records.csv ./data/raw/careroute_1000_clean_synthetic_demo_records.csv

USER careroute
EXPOSE 10000
CMD ["python3", "frontend/server/search_api.py"]
