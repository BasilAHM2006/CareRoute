# CareRoute dataset inspection report

**Inspection scope:** dataset and supplied college-project materials, read-only.  
**Dataset inspected:** `careroute_1000_clean_synthetic_demo_records.csv` (the root-level workspace copy, byte-identical to the inspected `Downloads/CareRoute/data/raw/` copy).  
**College material:** supplied `Document (1).docx` was fully extracted from its Word XML; the earlier supplied `Document.docx` contained the suggested-project list.  
**Interpretation:** CareRoute is the selected project. The student-performance material is an example, not a compulsory dataset specification.

## 1. Project overview

CareRoute helps patients and families discover and compare existing healthcare services. It does not employ providers and must not claim clinical suitability. Listings should be based on verified provider-service facts and link users to providers' official contact or booking channels. The inspected CSV is synthetic and cannot be treated as a factual directory.

## 2. Project directory inspection

The active writable workspace is `/Users/apple/Documents/CareRoute`. It has the root CSV and `reports/`. The selected project tree at `/Users/apple/Downloads/CareRoute/` contains `data/raw/`, `data/processed/`, `docs/`, `notebooks/`, `reports/`, and `src/`; the raw CSV is in `data/raw/`. The supplied `docs/Document (1).docx` is present there. The project reports directory at Downloads was not writable from this session, so these refreshed reports are saved in the active writable workspace's `reports/` directory. The original CSV and DOCX were not changed.

The `Downloads/CareRoute` structure had no project files in `data/processed/`, `src/`, `notebooks/`, or `reports/` at inspection; these folders were empty. `docs/` contains the DOCX (and a `.DS_Store`). `data/raw/` contains the CSV (and a `.DS_Store`). No XLSX or PDF was identified. The standalone earlier `Document.docx` was in a WhatsApp temporary documents path, not `docs/`.

## 3. College requirements and academic framing

The supplied materials include fifteen suggested project ideas, a general ten-step implementation workflow, and a separate worked student academic-performance example. CareRoute is the selected idea. The student example's student records, marks, and model variables do not become CareRoute requirements. The general workflow is the academic framework; adaptations of mathematical methods to provider data should be confirmed with the lecturer, especially inferential claims and predictive modelling.

The general workflow is: (1) define problem/objectives; (2) collect and understand 500–1,000+ records; (3) clean/preprocess; (4) descriptive statistics; (5) probability and hypothesis testing; (6) correlation and regression; (7) NumPy matrix operations, regression calculations and gradient descent; (8) develop/optimize model; (9) evaluate with MAE, MSE, RMSE, R² and residual analysis; (10) prepare final report and presentation. CareRoute-specific mappings are in `academic_requirements_checklist.md`.

## 4. Dataset overview and columns

The CSV has **1,000 rows, 20 columns**, and is **251,813 bytes**. This satisfies the workflow's record-count scale, but quantity does not establish authenticity or analytical adequacy. Fields are:

| Column | Meaning / interpretation |
|---|---|
| `record_id` | Synthetic row ID, CR####; unique here. Keep as text/key, not a numeric predictor. |
| `provider_name` | Generated placeholder such as Demo Provider 0001, not an actual organization. |
| `provider_type` | Generated provider category. |
| `service_name` | Generated service listing label. |
| `city`, `district`, `state` | Generated location labels; geographic validity unverified. |
| `experience_years` | Generated numeric experience value, years. |
| `rating_demo` | Generated rating; scale source and real reviews absent. |
| `estimated_hourly_cost_inr_demo` | Generated demo hourly price in INR, not a real quote. |
| `home_visit_demo` | Generated Yes/No flag. |
| `availability_demo` | Generated Yes/No flag, not time-stamped/current. |
| `injury_experience_demo` | Generated text label; not evidence of clinical qualification. |
| `mobility_support_demo` | Generated support label; actual capability unverified. |
| `languages_demo` | Generated language label(s), sometimes semicolon-separated. |
| `service_area_radius_km_demo` | Generated coverage radius, km. |
| `number_of_services_demo` | Generated count; its relationship to the one row's service is unspecified. |
| `verification_status` | Synthetic - not verified. |
| `data_source` | Generated synthetic demonstration data. |
| `record_type` | SYNTHETIC_DEMO_ONLY. |

### First 10 records (selected fields)

| record_id | provider_name | type | service | city | experience | rating | demo INR/hour | home visit | available |
|---|---|---|---|---|---:|---:|---:|---|---|
| CR0001 | Demo Provider 0001 | Rehabilitation Centre | Rehabilitation | Coimbatore | 1 | 3.5 | 500 | No | No |
| CR0002 | Demo Provider 0002 | Rehabilitation Centre | Stroke Rehabilitation | Nagercoil | 3 | 4.5 | 350 | No | Yes |
| CR0003 | Demo Provider 0003 | Elder Care Agency | Elder Care | Salem | 12 | 4.2 | 400 | Yes | Yes |
| CR0004 | Demo Provider 0004 | Nursing Service | Wound Care | Salem | 25 | 4.0 | 400 | Yes | Yes |
| CR0005 | Demo Provider 0005 | Rehabilitation Centre | Post-Injury Physiotherapy | Erode | 14 | 4.5 | 500 | No | Yes |
| CR0006 | Demo Provider 0006 | Nursing Service | Home Nursing | Nagercoil | 11 | 4.3 | 350 | Yes | Yes |
| CR0007 | Demo Provider 0007 | Home Healthcare Agency | Home Nursing | Erode | 25 | 5.0 | 450 | Yes | Yes |
| CR0008 | Demo Provider 0008 | Elder Care Agency | Elder Care | Tirunelveli | 24 | 4.2 | 400 | Yes | Yes |
| CR0009 | Demo Provider 0009 | Home Healthcare Agency | Elder Care | Thanjavur | 12 | 3.8 | 800 | Yes | Yes |
| CR0010 | Demo Provider 0010 | Home Healthcare Agency | Medication Support | Erode | 14 | 4.3 | 800 | Yes | No |

### Last 5 records (selected fields)

| record_id | provider_name | type | service | city | experience | rating | demo INR/hour | home visit | available |
|---|---|---|---|---|---:|---:|---:|---|---|
| CR0996 | Demo Provider 0996 | Physiotherapy Clinic | Home Physiotherapy | Madurai | 16 | 4.4 | 450 | Yes | Yes |
| CR0997 | Demo Provider 0997 | Physiotherapy Clinic | Home Physiotherapy | Madurai | 9 | 3.9 | 450 | Yes | Yes |
| CR0998 | Demo Provider 0998 | Home Healthcare Agency | Home Nursing | Thanjavur | 11 | 3.9 | 600 | Yes | No |
| CR0999 | Demo Provider 0999 | Physiotherapy Clinic | Rehabilitation | Tirunelveli | 6 | 4.1 | 800 | Yes | Yes |
| CR1000 | Demo Provider 1000 | Physiotherapy Clinic | Home Physiotherapy | Madurai | 2 | 4.3 | 450 | No | Yes |

**Runtime note:** Python's `csv` module was used to load the CSV. Pandas was not installed, so no Pandas DataFrame memory-usage figure is claimed. File size above is exact on-disk size. Numeric columns below were parsed from CSV strings; usual inferred types would be integer for experience/cost/radius/service count and float for rating. IDs remain strings; the other fields are text/categories.

## 5. Missing values

Blank-cell scan: **0 missing values** across 20,000 cells. The explicit category `Not specified` appears in `injury_experience_demo`; it is not a blank and should not be silently treated as null. No imputation is indicated for this file, although real-source completeness is unknown.

| Column set | Missing count | Treatment recommendation |
|---|---:|---|
| All 20 columns | 0 | No blank-value treatment indicated; retain explicit unknown labels and verify future source completeness. |

## 6. Duplicate analysis

- Exact duplicate rows: **0**.
- Duplicate `record_id` values: **0**; all 1,000 IDs are unique.
- Repeated provider names: **0**; all labels are unique generated placeholders.
- Repeated `(provider_name, service_name, city)` keys: **0**.

No duplicates were removed. Multiple service rows per real provider cannot be assessed because no provider repeats. Repeated service categories across different generated providers are expected and are not duplicate provider records.

## 7. Numerical variable analysis

All listed variables have 1,000 values. Variance/SD are sample statistics (`ddof=1`); quartiles use inclusive/linear interpolation. Modes include ties.

| Variable | Mean | Median | Mode | Min | Max | Variance | Std dev | Q1 | Q3 |
|---|---:|---:|---|---:|---:|---:|---:|---:|---:|
| `experience_years` | 12.6400 | 12 | 7 | 1 | 25 | 49.6621 | 7.0471 | 7 | 19 |
| `rating_demo` | 4.1903 | 4.2 | 4.3 | 3.0 | 5.0 | 0.1304 | 0.3611 | 3.9 | 4.4 |
| `estimated_hourly_cost_inr_demo` | 485.5500 | 450 | 450, 600 | 250 | 800 | 30459.1567 | 174.5255 | 350 | 600 |
| `service_area_radius_km_demo` | 21.3630 | 22 | 8 | 3 | 40 | 118.8801 | 10.9032 | 12 | 31 |
| `number_of_services_demo` | 4.5380 | 5 | 6 | 1 | 8 | 4.9055 | 2.2148 | 3 | 6 |

No univariate outliers were flagged by the 1.5×IQR fences for these five fields. That is a screening result, not validation of truth. All values appear plausible as generated demo values; provenance remains synthetic. `record_id` is not a meaningful numerical measurement.

## 8. Categorical variable analysis

There are 15 categorical/text fields, including the ID. Frequencies:

- `provider_type` (5): Rehabilitation Centre 236; Home Healthcare Agency 198; Nursing Service 197; Elder Care Agency 189; Physiotherapy Clinic 180.
- `service_name` (15): Rehabilitation 112; Elder Care 104; Home Nursing 101; Post-Injury Physiotherapy 98; Mobility Training 96; Stroke Rehabilitation 58; Companionship 55; Post-Surgery Nursing 55; Home Physiotherapy 52; Medication Support 51; Vital Signs Monitoring 50; Wound Care 47; Post-Surgery Care 41; Daily Living Assistance 41; Mobility Assistance 39.
- `city` (10): Tirunelveli 110; Nagercoil 106; Tiruchirappalli 106; Madurai 105; Chennai 104; Coimbatore 101; Thanjavur 101; Erode 99; Salem 84; Vellore 84.
- `district` (10): Tirunelveli 110; Kanniyakumari 106; Tiruchirappalli 106; Madurai 105; Chennai 104; Coimbatore 101; Thanjavur 101; Erode 99; Salem 84; Vellore 84.
- `state`: Tamil Nadu 1,000.
- `home_visit_demo`: Yes 698; No 302.
- `availability_demo`: Yes 753; No 247.
- `injury_experience_demo`: Back pain support 158; Not specified 156; Knee injury recovery 148; General mobility support 138; Stroke rehabilitation 138; Hip fracture recovery 137; Post-surgery recovery 125.
- `mobility_support_demo`: Walking assistance 212; Independent 209; Bedside assistance 198; Wheelchair assistance 193; Limited mobility 188.
- `languages_demo`: Tamil; Hindi 213; Tamil; Malayalam 209; Tamil; English 197; English 196; Tamil 185.
- `verification_status`: Synthetic - not verified 1,000.
- `data_source`: Generated synthetic demonstration data 1,000.
- `record_type`: SYNTHETIC_DEMO_ONLY 1,000.
- `provider_name` and `record_id`: 1,000 unique values each.

No capitalization variants were observed in the listed value categories. `Kanniyakumari` should be validated against an authoritative geographic reference before any normalization. City and district happen to align in most rows but should be distinct fields. Languages are multi-valued text. `Not specified` is an explicit unknown category.

## 9. Authenticity and limitations

**Classification: entirely synthetic demonstration data, explicitly unverified.** Every row identifies a generated data source and `SYNTHETIC_DEMO_ONLY` record type; provider names are numbered demo placeholders. There are no actual organizations, primary-source citations, official websites, contact details, booking links, verification dates, or source evidence. Ratings, prices, home visits, availability, provider experience, injury-support categories, mobility capabilities, languages and service coverage are generated demonstration attributes. Do not expose them as factual provider information or use them to recommend a real provider. Do not invent replacement links or facts.

The file has no patient age, patient weight, prior patient injury/surgery data, actual provider identity, customer outcomes, service demand, booking/referral outcomes, or measured clinical outcomes. It cannot establish clinical suitability, provider quality, actual availability, real prices, or real geographic coverage.

## 10. CareRoute academic compatibility: current data versus proposed analysis

| Method / workflow area | Current dataset status | CareRoute use and limitation |
|---|---|---|
| Data loading, cleaning, type identification, missing/duplicate checks | Supported for demonstration | Inspect the schema and synthetic rows; retain provenance and do not misrepresent the records. |
| Descriptive statistics / distributions | Supported for demo values | Summarize synthetic listing fields only; do not infer real-market distributions. |
| Sampling and hypothesis testing | Partially supported | Can demonstrate methods on generated records. Population claims or tests comparing real service/provider groups require sourced representative observations; lecturer approval for the adapted question. |
| Probability, conditional probability, Bayes, law of large numbers | Partially supported | Events such as demo `availability_demo=Yes` can illustrate calculations, but generated records are not provider-population probabilities. Apply to authentic, defined events only for substantive claims. |
| Pearson/Spearman/correlation matrix | Partially supported | Can calculate among numeric demo fields; correlations may reflect generation rules and do not imply real-world relationships. Exclude IDs. |
| Regression and prediction | Not supported substantively | No verified continuous outcome or meaningful source-backed predictor/target pair. A real cost model could be considered only after consistent, verified quotes and an explicit prediction question are collected; lecturer approval needed. |
| Linear algebra (vectors, matrices, addition, multiplication, dot products) | Supported as a classroom demonstration | Use numeric columns to demonstrate mechanics; clearly label demo data. A regression matrix needs a defensible target. |
| Cost function, derivatives, gradient descent, optimization | Not supported for valid modeling | No defensible prediction target. Do not fabricate labels. Can be taught after a lecturer-approved target/data source is chosen. |
| MAE, MSE, RMSE, R², actual/predicted, residual plots | Not supported | These require an observed outcome and valid held-out predictions. |

The labels above concern the inspected file; the workflow itself is the academic framework. Proposed healthcare adaptations and lecturer-approval points are itemized in the checklist.

## 11. Additional data needed

### Dataset A — factual provider-service directory for CareRoute

Collect listing-level records with Provider ID, provider name, provider type, service name, specialization, city, district, state, home-visit availability, service coverage, official website, contact details, booking link, source, verification date and verification status. Also preserve source URL/evidence and a last-checked date. Confirm claims from provider-controlled or otherwise authoritative sources; distinguish unknown, not applicable and unverified. Keep separate rows for real provider-service-location combinations where appropriate. This directory supports discovery and logistics filtering, not clinical decisions.

### Dataset B — optional academic statistics/modeling data

A second dataset is needed only if required techniques include meaningful inferential or predictive modeling and Dataset A does not offer a valid target. Options for lecturer approval: (a) sourced, time-stamped, comparable service quote observations with target cost and features such as service type, visit type, duration and location; or (b) another relevant public/approved healthcare-service operations dataset with a clearly measured numeric outcome. Document source, units, sampling frame, time period, limitations and target definition. Do not mix it with the directory without an analytical reason. Do not use patient-sensitive characteristics to predict clinical suitability.

## 12. Recommended preprocessing strategy (recommendations only)

1. Preserve original raw files; perform work in a derived dataset with provenance.
2. Distinguish actual nulls from explicit `Not specified`, unavailable, unknown and not applicable.
3. Check exact duplicates and listing-key collisions, then adjudicate using source evidence; preserve legitimate multiple service/location listings.
4. Parse numeric measures with errors surfaced; retain IDs as strings, flags/categories as categorical, and dates as dates.
5. Standardize derived column names to snake_case; retain original field names/source values in lineage.
6. Validate geographic labels against an authoritative reference and store normalized value plus source label.
7. Use controlled vocabularies for service/type/flags; normalize multilingual fields as structured values while preserving source text.
8. Check numerical ranges and units from trusted evidence. Use IQR and domain/source review for outliers; never auto-delete plausible records.
9. Encode nominal categories with suitable one-hot/multi-label methods only for a defined analysis; exclude IDs and provenance fields from predictors.
10. Select features only after defining a meaningful target. Split train/test by provider/entity or time where needed to avoid leakage; fit imputation/encoding/scaling on training data only.

No cleaning was applied and no CSV was modified.

## 13. Recommended next steps

1. Confirm with the lecturer that CareRoute is the chosen topic and which parts of the general workflow need formal analysis/modeling.
2. Keep this CSV clearly labeled as synthetic UI/demo data.
3. Build Dataset A through careful, traceable verification of actual provider-service facts; do not invent details.
4. If regression/calculus/model-evaluation tasks are required, agree with the lecturer on a coherent sourced Dataset B, prediction target, and scope before collecting or modeling.
5. Then plan analysis and development; do not treat a provider recommender as a medical decision system.

## Method note

The CSV was loaded with Python's standard-library `csv` module because Pandas was unavailable in the active environment; no packages were installed. DOCX main-document XML was fully extracted and read. No web verification, cleaning, model fitting, or application development was performed.
