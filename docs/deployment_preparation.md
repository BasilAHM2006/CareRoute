# CareRoute deployment preparation

## Architecture

- Render Static Site builds and publishes only `frontend/dist`.
- Render Docker Web Service runs the Python API and the immutable SQLite search index.
- The Docker build has two stages. The builder reads the existing raw and cleaned datasets, checks row and identifier parity, and generates the index with the pinned Pandas/PyArrow versions. The final runtime image contains the API, the index, the Nagercoil pilot CSV, and the separate synthetic CSV; it excludes the raw and cleaned facility datasets, project reports, docs, and templates.
- The SQLite file is generated from the cleaned public facility dataset and served read-only. No Render persistent disk is required. Startup validates SQLite integrity, the full API schema, row/FTS counts, and the expected 166,462 facility, 4 provider, 16 service-offer, and 1,000 demo-record counts before accepting requests.
- The frontend uses `VITE_API_BASE_URL` in production and keeps relative `/api` requests in local development. The static host rewrites provider and facility detail routes to `index.html`.

## Security and data boundaries

- The GitHub repository must be private. `.gitignore` excludes local environments, dependencies, generated index/build output, local env files, and credentials.
- `.dockerignore` applies a narrow allowlist. The static site publishes `frontend/dist` only; it does not publish `data/`, `docs/`, or `reports/`.
- `CAREROUTE_ALLOWED_ORIGINS` must list the exact deployed frontend origin(s). CORS allows read-only GET/OPTIONS requests and does not enable credentials or wildcard origins.
- Render's assigned `PORT` is used by the API, which binds to `0.0.0.0` in the container.
- Production API errors return generic client messages; diagnostic details go to service logs. JSON responses include `nosniff` and `no-store` headers.
- The demo endpoint still filters for `record_type=SYNTHETIC_DEMO_ONLY`; the frontend also rejects unexpected non-demo records before displaying the preview.

## Deployment settings

`render.yaml` defines `careroute-api` (Docker, 1 CPU/2 GB plan) and `careroute-web` (static site). Automatic deploys are disabled. The default configured public origins are `https://careroute-web.onrender.com` and `https://careroute-api.onrender.com`; update both values if Render assigns different service subdomains.

Never put API secrets in `VITE_*` variables: Vite embeds them into public browser assets. This project has no API credentials or secret variables at present.

## Before a first deployment

1. Review all tracked files and confirm any data reuse terms allow private-repository and API-based use.
2. Create a new private GitHub repository; do not publish this project as a public repository.
3. Push the project including only approved required source files. Do not commit `.venv/`, `frontend/node_modules/`, `frontend/dist/`, `frontend/.data/`, or `.env` files.
4. Connect the private repository to Render and create services from `render.yaml`. `autoDeploy: false` prevents subsequent pushes from deploying automatically.
5. Confirm the actual generated service URLs. Set the exact frontend origin in the API's `CAREROUTE_ALLOWED_ORIGINS`, and the API URL in the frontend's `VITE_API_BASE_URL`, then rebuild/redeploy both services.
6. Validate `/api/health` reports 166,462 facilities, 4 pilot organizations, and 1,000 synthetic demo records. Smoke-test facility search, details, options, provider service filters, and demo isolation before sharing the URL.

## Current validation scope

Local tests validate the generated index and existing source records without modifying them, exercise the search and filter functions directly, and verify the static publish directory contains no source dataset files. The current execution environment blocks loopback socket binding, so HTTP-level requests could not be run locally. The live Render build, CORS against the final hostnames, TLS, service health check, and final public URL require account connection and deployment approval.
