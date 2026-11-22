# CareRoute

CareRoute is a responsive healthcare discovery interface for India, beginning with Tamil Nadu and Nagercoil. It keeps public facilities, provider-reported pilot records and synthetic demonstration records in separate discovery views.

## Run locally

From this directory, run:

```sh
npm run dev
```

The command starts Vite and the read-only Python search API. It uses the project’s existing `../.venv` and its Pandas/PyArrow installation. On first start, the API builds an ignored local SQLite/FTS index under `frontend/.data/` from `data/processed/india_healthcare_cleaned.parquet`. It checks the original Parquet row count and confirms the cleaned CSV has the same `entity_uid` sequence. The raw and processed source datasets are read-only.

The Vite app is normally available at `http://127.0.0.1:5173`. The API binds to `127.0.0.1:8787` and is reached by Vite through its `/api` proxy.

## Data views

- **Public facilities:** paginated, indexed search across the existing cleaned national facility dataset. Its original `entity_uid` remains attached to each result. Registry inclusion does not establish current operation or any specific service.
- **Local care providers:** the 16 service rows in the Nagercoil pilot are grouped into four provider cards. Service and home-visit claims remain attributed to provider-reported phone contact.
- **Preview demo:** synthetic rows are served separately and visibly marked `DEMO DATA`; they are never merged with real listings.

The public dataset has no demonstrated service-availability evidence, so service-specific results come only from the Nagercoil pilot. No clinical suitability is inferred.

## Build

```sh
npm run build
```

The front end uses the dependencies already present in this project. The local search API uses Python’s standard library plus the existing Pandas and PyArrow packages; no package installation is required.
