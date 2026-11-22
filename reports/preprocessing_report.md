# Preprocessing report: India public healthcare facilities

## Run and file verification

- Working directory: `/Users/apple/Downloads/CareRoute`
- Source: `data/raw/india_public_healthcare.parquet`
- Source SHA-256 before: `edfea7aacb44f747c99c6594f5ac32623ab28000dd43e2dcd4503fae5c29574b`
- Source SHA-256 after: `edfea7aacb44f747c99c6594f5ac32623ab28000dd43e2dcd4503fae5c29574b`
- Source hash unchanged: **True**
- Read engine: Pandas with PyArrow (`pandas 3.1.1`, `pyarrow 26.0.1`)
- Processed Parquet: `data/processed/india_healthcare_cleaned.parquet`
- Processed CSV: `data/processed/india_healthcare_cleaned.csv`
- Processed Parquet reload: successful; `166,462` rows; `26` columns.

## Record and column counts

- Original records: **166,462**
- Processed records: **166,462**
- Record-count difference: **0**
- Original columns: **17**
- Processed columns: **26** (all 17 source columns retained; 9 documented derived/audit columns added)

## Missing values before cleaning

The source has 0 Pandas nulls. Its text fields also use literal missing markers. The table reports physical nulls and recognized marker counts separately; the last column combines them for an effective missingness estimate.

| Column | Physical nulls | Physical null % | Recognized markers | Effective missing % |
| --- | --- | --- | --- | --- |
| entity_uid | 0 | 0.000% | 0 | 0.000% (physical + recognized markers) |
| facility_name | 0 | 0.000% | 12 | 0.007% (physical + recognized markers) |
| facility_type | 0 | 0.000% | 0 | 0.000% (physical + recognized markers) |
| state | 0 | 0.000% | 0 | 0.000% (physical + recognized markers) |
| district | 0 | 0.000% | 1 | 0.001% (physical + recognized markers) |
| taluka | 0 | 0.000% | 9797 | 5.885% (physical + recognized markers) |
| block | 0 | 0.000% | 26793 | 16.096% (physical + recognized markers) |
| address | 0 | 0.000% | 50712 | 30.465% (physical + recognized markers) |
| street | 0 | 0.000% | 55862 | 33.558% (physical + recognized markers) |
| landmark | 0 | 0.000% | 64253 | 38.599% (physical + recognized markers) |
| locality | 0 | 0.000% | 38663 | 23.226% (physical + recognized markers) |
| pincode | 0 | 0.000% | 16387 | 9.844% (physical + recognized markers) |
| landline_number | 0 | 0.000% | 137921 | 82.854% (physical + recognized markers) |
| longitude | 0 | 0.000% | 0 | 0.000% (physical + recognized markers) |
| latitude | 0 | 0.000% | 0 | 0.000% (physical + recognized markers) |
| geometry | 0 | 0.000% | 0 | 0.000% (physical + recognized markers) |
| source | 0 | 0.000% | 0 | 0.000% (physical + recognized markers) |

Recognized marker counts by field:

{
  "facility_name": {
    "NA": 12
  },
  "district": {
    "\\N": 1
  },
  "taluka": {
    "\\N": 9797
  },
  "block": {
    "NA": 27,
    "\\N": 26766
  },
  "address": {
    "-": 296,
    "0": 868,
    "NA": 45014,
    "\\N": 4534
  },
  "street": {
    "-": 129,
    "0": 374,
    "NA": 49765,
    "\\N": 5594
  },
  "landmark": {
    "-": 128,
    "0": 228,
    "NA": 63897
  },
  "locality": {
    "-": 65,
    "0": 160,
    "NA": 38438
  },
  "pincode": {
    "NA": 16387
  },
  "landline_number": {
    "-": 682,
    "0": 1954,
    "N/A": 91,
    "NA": 134446,
    "NIL": 168,
    "NO": 67,
    "Nil": 270,
    "No": 93,
    "Not available": 56,
    "nil": 94
  }
}

## Missing values after cleaning

Missing markers were replaced with Pandas nulls according to the column-specific rules below. These counts are for the 17 retained source columns after cleaning; derived validation flags remain false/true or null as appropriate.

| Column | Nulls after cleaning | Percent |
| --- | --- | --- |
| entity_uid | 0 | 0.000% |
| facility_name | 12 | 0.007% |
| facility_type | 0 | 0.000% |
| state | 0 | 0.000% |
| district | 1 | 0.001% |
| taluka | 9797 | 5.885% |
| block | 26793 | 16.096% |
| address | 50712 | 30.465% |
| street | 55862 | 33.558% |
| landmark | 64253 | 38.599% |
| locality | 38663 | 23.226% |
| pincode | 16387 | 9.844% |
| landline_number | 137921 | 82.854% |
| longitude | 0 | 0.000% |
| latitude | 0 | 0.000% |
| geometry | 0 | 0.000% |
| source | 0 | 0.000% |

## Duplicate analysis

- Exact duplicate source rows: **0**.
- Duplicate `entity_uid` excess rows (duplicates after first): **0**; rows participating in duplicate-ID groups: **0**.
- Repeated facility names, normalized by trimming and case-folding: **27,315 excess rows** among **27,315 repeated-name rows**.
- No rows were removed. Facility-name repetition was retained and flagged in `facility_name_duplicate`; IDs were retained and flagged in `facility_id_duplicate`.

## PIN-code validation

- PIN values after marker normalization: **150,075 nonmissing**, **16,387 missing**.
- Among nonmissing PIN values, six-digit numeric-string format: **150,075 valid**, **0 invalid**.
- The 16,387 source values that failed the format check were all literal `NA`; they are null after cleaning, leaving 150,075 valid-format values and zero invalid nonmissing values. `pincode_valid` is nullable so missing PINs are not represented as validated.
- Format checking does not validate that a PIN exists or matches the facility location.

## Coordinate validation

- Coordinate pairs present after cleaning: **166,462**; incomplete/missing pairs: **0**.
- Values outside global latitude/longitude ranges: **0**.
- Pairs outside the approximate India bounds (latitude 6–38.5, longitude 68–97.5): **10**.
- The outside-boundary pairs are retained and flagged in `coordinates_outside_india_bounds`; `coordinates_valid` checks global coordinate ranges and presence only.
- Approximate bounding-box checks do not establish facility-level positional accuracy. State/district-to-coordinate validation remains unresolved and should be done against authoritative boundaries or facility records.

## Facility-type distribution

The source labels are retained in `facility_type` after whitespace/missing cleanup. The standardized values are in `facility_type_standardized`.

| Standardized category | Records | Share |
| --- | --- | --- |
| Sub-centre | 133033 | 79.918% |
| Primary health centre | 21779 | 13.083% |
| Community health centre | 4502 | 2.705% |
| Other health facility | 2186 | 1.313% |
| Urban health centre | 1425 | 0.856% |
| Sub-district hospital | 850 | 0.511% |
| Dispensary | 710 | 0.427% |
| District hospital | 592 | 0.356% |
| Urban health post | 438 | 0.263% |
| Hospital (<100 beds) | 174 | 0.105% |
| M&CW centre | 153 | 0.092% |
| Medical college hospital | 147 | 0.088% |
| Civil/general hospital | 110 | 0.066% |
| Maternity home | 100 | 0.060% |
| Postpartum unit | 84 | 0.050% |
| Hospital (100-500 beds) | 62 | 0.037% |
| Referral hospital | 56 | 0.034% |
| Women hospital | 30 | 0.018% |
| AYUSH dispensary | 17 | 0.010% |
| Hospital (>500 beds) | 14 | 0.008% |

Documented one-to-one mapping (all 20 observed labels; no categories were merged):

| Source label | Standardized label |
| --- | --- |
| SubCentre | Sub-centre |
| Primary Health Centre | Primary health centre |
| Community Health Center | Community health centre |
| Others | Other health facility |
| Urban Health Centre | Urban health centre |
| Sub-District Hospital | Sub-district hospital |
| Dispensaries | Dispensary |
| District Hospital | District hospital |
| Urban Health Posts | Urban health post |
| <100 Bedded Hospital | Hospital (<100 beds) |
| M&CW Center | M&CW centre |
| Medical Colleges Hospital | Medical college hospital |
| Civil Hospital/General Hospital | Civil/general hospital |
| Maternity Home | Maternity home |
| Post Partum Unit | Postpartum unit |
| 100-500 Bedded Hospital | Hospital (100-500 beds) |
| Referral Hospital | Referral hospital |
| Women Hospital | Women hospital |
| Ayush Dispensaries | AYUSH dispensary |
| >500 Bedded Hospital | Hospital (>500 beds) |

## Geographic spelling standardization

Original values are retained in `state_original` and `district_original`. Standardized fields replace only the documented aliases below:

| Field | Source value | Standardized value |
| --- | --- | --- |
| state | Telengana | Telangana |
| district | BALRAMPUR | Balrampur |

All other state/district spellings remain as found because no authoritative gazetteer was used to establish additional aliases. District names shared across states may be legitimate and were not treated as errors.

## Every transformation performed

1. Loaded the source Parquet with Pandas/PyArrow and made an in-memory deep copy; the source file was never written.
2. Trimmed leading/trailing whitespace in string columns.
3. Converted exact `NA` and `\N` markers to null for descriptive/geographic text fields, excluding `entity_uid` and `source`.
4. Treated `-` and `0` as missing only in `address`, `street`, `landmark`, and `locality`.
5. Treated `-`, `0`, `Nil`, `NIL`, `nil`, `No`, `NO`, `N/A`, and `Not available` as missing only in `landline_number`.
6. Kept `pincode` and `landline_number` as text; applied six-digit PIN format validation and added nullable `pincode_valid`.
7. Added `state_original`, `district_original`, and `facility_type_original` trace fields before canonicalization.
8. Standardized the one observed state spelling alias (`Telengana` → `Telangana`) and district casing alias (`BALRAMPUR` → `Balrampur`); added no inferred values.
9. Added `facility_type_standardized` using the explicit one-to-one mapping above; retained original source categories in `facility_type` and `facility_type_original`.
10. Added `coordinates_valid` (pair present and both values in global ranges) and `coordinates_outside_india_bounds` flags using the bounds stated above.
11. Added `facility_id_duplicate` and `facility_name_duplicate` flags. Repeated names were not deduplicated and no records were dropped.
12. Kept all 17 original columns. Added 9 audit/trace columns: `state_original`, `district_original`, `facility_type_original`, `facility_type_standardized`, `pincode_valid`, `coordinates_valid`, `coordinates_outside_india_bounds`, `facility_id_duplicate`, `facility_name_duplicate`.
13. Wrote Parquet with PyArrow-backed Pandas serialization. For CSV only, encoded WKB geometry bytes as hexadecimal text so the geometry remains representable in a text file; the Parquet geometry remains binary WKB.

## Unresolved data-quality issues

- No record-level verification timestamp or operational status is present in the inspected schema; current availability is not established by preprocessing.
- Literal placeholders are widespread, especially for landline numbers, addresses, landmarks, locality, and block; these are missing information, not negative/verified facts.
- 16,387 PIN values are missing after marker normalization; six-digit format alone is not authoritative PIN validation.
- Ten coordinates fall outside the approximate India bounds; additional coordinates may be inaccurate despite passing that broad test.
- District spellings and administrative naming can be legacy or inconsistent; only explicitly observed, low-risk aliases were standardized.
- Repeated names are common (27,315 excess normalized name occurrences) and are not sufficient evidence of duplicate facilities.
- `facility_type` describes the facility classification only; it does not establish nursing, physiotherapy, home-visit, hours, capacity, or service availability.
- The source field attributes records to the MoHFW/NHSRC NIN-to-HFI registry (2025) via data.gov.in. This processing did not independently refresh or verify source records.

## Validation results

- Processed Parquet reopened successfully using Pandas/PyArrow.
- Reloaded schema columns and order match the written processed dataset.
- Reloaded processed record count matches source: **166,462 = 166,462**.
- Reloaded processed column count: **26**.
- Original Parquet SHA-256 after processing: `edfea7aacb44f747c99c6594f5ac32623ab28000dd43e2dcd4503fae5c29574b`.
- Original hash unchanged: **True**.
