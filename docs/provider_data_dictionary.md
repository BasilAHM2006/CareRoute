# CareRoute provider data dictionary (proposed)

**Status:** Proposed schema; no provider records have been collected.  
**Geography:** India.  
**Record grain:** One row per provider × service × delivery location/area. Keep provider identity separate from location and service offers. A provider offering multiple services or operating at multiple sites may have multiple rows sharing the same stable `provider_id`; do not create duplicate identities to model services.

## Core rules

- Store only source-backed facts. Unknown, not stated, not checked, and not applicable are distinct; never convert missing facts to `No` or a positive claim.
- Preserve the raw source value and source URL for any standardized/canonical value.
- Individual professional and caregiver listings require a documented lawful basis and consent for public listing. Do not store Aadhaar, personal addresses, private phone numbers, patient information, or unnecessary identifiers.
- The taxonomy in `docs/provider_service_taxonomy.md` supplies the controlled service categories and separate entity types.
- This schema is for discovery of existing services. It does not rank clinical suitability or create a job/employment profile marketplace.

## Proposed directory fields

| Field | Type / allowed values | Required? | Definition and validation |
|---|---|---:|---|
| `provider_id` | String | Yes | CareRoute stable internal opaque ID; generated only for an evidence-backed provider, not a source claim. Never reuse synthetic demo IDs. |
| `source_record_id` | String | Conditional | Source's record/registry ID, if publicly available and permitted to store. Preserve as text. |
| `provider_name` | String | Yes | Public organization, facility, residence, practice, or consenting individual's professional display name, exactly traceable to a source. |
| `legal_entity_name` | String | No | Legal organization name where a reliable official source confirms it. Keep separate from trading/brand name. |
| `brand_name` | String | No | Public brand associated with the legal entity. |
| `provider_type` | Enum | Yes | `healthcare_facility`, `home_healthcare_company`, `individual_professional`, `geriatric_caregiver`, `residential_care_provider`, `mental_health_service`, `other_organization`. Select one primary listed entity class; explain exceptional cases. |
| `provider_type_detail` | String / controlled detail | No | E.g. hospital, clinic, nursing agency, senior residence. Must not substitute for service categories. |
| `service_id` | String | Yes | Stable ID for the provider-service-location offer. Multiple services get separate rows or linked service records. |
| `service_name` | String | Yes | Source-backed public name/description of this service. Preserve a separate `service_name_source` if normalized. |
| `service_category_code` | Enum from taxonomy | Yes | One code from the CareRoute taxonomy. Multiple categories require evidence for each. |
| `service_subcategory` | String | No | More specific source-backed service label; do not infer from provider type. |
| `service_description` | String | No | Concise factual summary supported by the cited source. Do not copy protected marketing text at length. |
| `delivery_modes` | Multi-value enum | Yes | `at_facility`, `home_visit`, `remote`, `residential`, `community`, `not_stated`. Use `not_stated` until a source establishes mode. |
| `service_status` | Enum | Yes | `verified_available`, `verified_unavailable`, `not_stated`, `not_checked`, `expired`. Availability must be locality- and time-specific where applicable. |
| `service_status_checked_at` | ISO date/datetime | No | Date/time at which this service status was confirmed. |
| `home_visits_available` | Enum: `yes`, `no`, `not_stated`, `not_checked`, `expired` | Yes | Do not infer from an organization's name or general home-health category. |
| `home_visit_services` | String/list | No | Only service names explicitly confirmed for home visits. |
| `home_visit_coverage` | String/list | No | Confirmed cities/districts/postal areas served at home, with a source for each claim. |
| `service_location_id` | String | Yes | Stable ID for physical location/service catchment row. One provider can have many. |
| `country` | String | Yes | `India` for current scope. |
| `state_or_ut` | String | Conditional | Canonical State/UT with source spelling retained in `state_source_value`. |
| `district` | String | No | Canonical district when verified; retain `district_source_value`. |
| `city_or_locality` | String | No | Locality/city exactly backed by source. |
| `postal_code` | String | No | String format, validated against an authoritative postal source if possible. Never coerce to number. |
| `address_public` | String | No | Public facility/business address only; not an individual's private residence. |
| `latitude` / `longitude` | Decimal | No | Coordinates with `coordinate_source`, `coordinate_accuracy_note`, and verification; do not geocode/invent when absent. |
| `service_area_description` | String | No | Explicit service area, not a guessed radius. |
| `contact_phone_public` | String | No | Public organizational/business contact only; preserve formatting and source. |
| `contact_email_public` | String | No | Public organizational/business email only. |
| `official_website_url` | URL | No | Provider-controlled official URL; validate ownership and current operation. |
| `official_service_url` | URL | No | Specific official service/location page, if available. |
| `booking_or_enquiry_url` | URL | No | Official booking/enquiry route. Do not claim real-time appointment availability unless verified. |
| `operating_hours` | String / structured schedule | No | Published hours, with source and last-checked date. `not_stated` if absent. |
| `professional_name_public` | String | Conditional | Individual professional's public name only when consented and lawful; use sparingly. Not needed for organisation-only records. |
| `professional_role` | String | Conditional | E.g. registered nurse, physiotherapist, geriatric caregiver. Distinguish regulated and non-regulated roles. |
| `qualification_claim` | String | Conditional | Exact qualification and awarding institution only where source-backed. Do not infer from job title. |
| `registration_council` | String | Conditional | Applicable statutory/professional council, where relevant. |
| `registration_number_public` | String | Conditional | Store only when needed, publicly searchable, permitted, and not a sensitive ID; validate with issuing authority. |
| `registration_status` | Enum: `active_verified`, `inactive`, `not_applicable`, `not_checked`, `unknown` | Conditional | Checked with issuing council/register; include validity/checked date and source. |
| `residential_setting_type` | String / controlled value | Conditional | E.g. assisted living, senior living, care home, hospice. Only for residential locations. |
| `residential_admission_status` | Enum: `open_verified`, `closed_verified`, `not_stated`, `not_checked`, `expired` | No | Do not imply vacancies/capacity unless verified at the time shown. |
| `source_id` | String | Yes | Key referencing `data/raw/provider_source_inventory.csv`. |
| `source_name` | String | Yes | Human-readable source name. |
| `source_url` | URL | Yes | Exact page or registry record supporting this row, not just a home page when a detail page exists. |
| `evidence_note` | String | Yes | What the source supports and any limitation; short factual note, not a copied source passage. |
| `source_checked_at` | ISO date/datetime | Yes | When source was reviewed. |
| `verification_status` | Enum | Yes | `unverified`, `source_checked`, `independently_verified`, `expired`, `disputed`, `withdrawn`. |
| `verification_method` | Enum/text | Yes | E.g. registry check, provider official page, direct confirmation with provider, council check. State what was checked. |
| `last_verified_at` | ISO date/datetime | Conditional | Date of latest identity/service/contact/qualification check. Separate dates may be needed for distinct claims. |
| `next_review_due_at` | ISO date/datetime | No | Recency policy deadline; listings become stale/expired after the defined interval. |
| `data_licence_name` | String | Yes | License/terms applicable to the source and fields. Use `not_confirmed` until verified. |
| `data_licence_url` | URL | No | Exact license/terms URL. |
| `reuse_permission_status` | Enum: `open_license_confirmed`, `permission_granted`, `public_facts_only_reviewed`, `not_confirmed`, `permission_denied` | Yes | Do not infer that public accessibility permits republication. |
| `attribution_text` | String | Conditional | Required source attribution text where license/permission requires it. |
| `individual_listing_consent` | Enum: `yes_documented`, `no`, `not_applicable`, `not_checked` | Yes | For an individual person's public profile; `yes_documented` requires consent evidence and date. |
| `privacy_review_status` | Enum: `passed`, `needs_review`, `not_applicable` | Yes | Check necessity, public status, consent/lawful basis and no private/patient data. |
| `record_created_at` | ISO datetime | Yes | CareRoute import/create timestamp. |
| `record_updated_at` | ISO datetime | Yes | Latest change to the CareRoute record. |
| `data_quality_notes` | String | No | Unresolved issues, ambiguity, stale source, conflict or limitation. |

## Verification state meanings

- `unverified`: discovered as a candidate only; not publishable as verified.
- `source_checked`: a source page was reviewed, but identity, active status or claim was not independently confirmed.
- `independently_verified`: identity and the specific published claims (service, location, contact and relevant qualification) were confirmed using authoritative evidence and are within the freshness window.
- `expired`: evidence is too old or service status cannot be reconfirmed; suppress time-sensitive claims until refreshed.
- `disputed`: credible conflicting information exists; hide or clearly withhold the contested claim pending resolution.
- `withdrawn`: provider/requester/source removed the listing or permission ended; retain only minimal audit lineage as allowed.

A provider may have a verified identity but an unverified service or location. Keep verification at claim level where possible; do not let one verified field upgrade every field on the row.
