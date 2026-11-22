# CareRoute provider collection workflow

**Status:** Preparation only; no provider records collected.  
**Coverage objective:** All India, across health facilities, home healthcare, elderly care, rehabilitation, personal care and relevant support services.  
**Pilot target:** Build toward 50–100 real organization-service-location rows after access and reuse approval. The template is empty until actual records are sourced and checked.

## 1. Data model and record boundaries

Use one pilot row for one **organization × service × physical location or explicitly verified service area**. A provider with three services in two cities can generate up to six rows if each offer is explicitly supported; all rows share the same provider identity and locations have their own stable IDs. Do not create a new provider for each service, infer a branch from a company city list, or copy a synthetic demonstration row.

Keep distinct:

- **Home nursing:** an explicit nursing offer at home; verify service, visit mode, territory and regulated nursing credentials where named.
- **Physiotherapy:** clinic or home service offer; keep clinic and home delivery separate; do not equate rehabilitation-centre listing with any particular treatment.
- **Elderly care:** clinical and non-clinical services must be separate. “Caregiver,” “attendant,” “nurse,” and “geriatric professional” are not interchangeable.
- **Home healthcare:** delivery setting/cross-cutting tag; it does not prove that every service on a company website is delivered at home or in every city.
- **Rehabilitation centres:** physical facilities, with specific disciplines/programs verified at centre level.
- **Hospitals and clinics:** physical healthcare facilities; a government registry listing is an identity lead, not proof of service, current operation, or home visits.
- **Other services:** diagnostic, palliative, disability support, personal care, mental health, residential care and medical support, each with explicit source evidence.
- **Organizations vs people vs facilities:** company/provider identity, named individual professional, caregiver profile and each physical branch are separate entities. The current Phase 4 pilot is organization-service-location oriented; person-level caregiver/professional listings are out of scope unless a separate consent, privacy and verification approval is made.

Use `docs/provider_service_taxonomy.md` for service codes and `docs/provider_data_dictionary.md` for the complete field dictionary and status meanings.

## 2. Source priority and permitted collection

### Priority A — official facility and credential verification

1. **ABDM HFR** for a facility identity/registry lead. Confirm whether the record and service attributes can lawfully be accessed and reused. No use of HFR APIs or exports without explicit access approval and source terms review.
2. **HPR and applicable statutory councils** for individual credential verification only where individual listings are in an approved scope. HPR does not prove an individual is accepting patients or offers home service. For nurses, verify a current State/UT Council practice registration; NRTS/NUID enrollment by itself is not that practice licence.
3. **RCI/CRR** for the professional categories within RCI’s statutory register, not all mental-health, disability or rehabilitation providers.
4. **Existing India public-healthcare dataset** can seed facility leads only after provenance/reuse review and record-by-record confirmation. Its current schema lacks service offerings, home visits, open status and appointment availability.

### Priority B — provider-controlled service and location claims

Begin with the inventory candidates Portea, Apollo HomeCare, HCAH and Nightingales, then Antara and Emoha for senior/residential/home-care coverage. Their sites provide candidate service descriptions, booking/contact channels and sometimes selected cities. Check each specific service-city combination directly. Resolve legal entity, brand, ownership and branch identity before creating records. Provider pages do not independently verify qualifications of all staff and terms do not grant open database-reuse rights.

### Priority C — other official and specialist sources

Use SHATAYU only as a possible caregiver-directory lead after legal, consent and product-scope review. It is a person-level caregiver connection/directory, not a company/facility source; the pilot should not ingest its personal profiles by default. Tele-MANAS is a public mental-health support resource, not a provider directory row. Other service organizations can be added to the source inventory only after finding their official site and checking current services, operating areas and reuse terms.

### Collection methods allowed only after permission

- Manually review specific public pages and capture a small set of factual fields with source URL/date, if site terms permit it.
- Contact the organization or source authority using official contact channels to request permission and confirmation.
- Use APIs, bulk downloads, or structured exports only after explicit source authorization, technical onboarding where required, and documented licence/privacy review.
- No scraping, automated browser extraction, rate-limit circumvention, authenticated-user data harvesting, third-party aggregator harvesting, or copying of prose/images in this phase. A source page found by search is a lead, not a collected row.

## 3. Pilot staging toward 50–100 rows

The pilot is a validation exercise, not a claim of national completeness.

1. Agree the pilot’s States/UTs or serviceable cities, while retaining the All-India expansion target. Select geographies based on source access and service diversity, not assumptions that an area has providers.
2. Create a source permission register: organization/source contact, permission basis, licence/terms version/date, approved fields, allowed storage/display, API/export conditions, retention and attribution.
3. Capture only organization/facility-service-location records first. Maintain one source-evidence row per claim and place candidates in an internal unverified queue. Do not fill the published template with speculative leads.
4. Aim for 50–100 **verified** organization-service-location rows across the approved pilot area and categories. Multiple services/locations may refer to the same organization. Do not pad the target with duplicate names, synthetic records or unverified data.
5. If source permission or substantiation does not support 50 verified rows, keep the actual smaller count and report the gap; do not lower standards or fabricate entries.
6. Expand state by state using a coverage ledger for states, districts, categories, source, rows researched, rows verified, and not-yet-checked areas. “No records collected” means unknown coverage, not “no provider exists.”

## 4. Record-level collection workflow

1. **Open a source lead.** Record source ID from `data/raw/provider_source_inventory.csv`, exact official URL, access date, and source type. Verify the domain and whether the page is controlled by the named provider/authority.
2. **Confirm organization identity.** Capture source-backed public name, legal entity, brand, registry/business identity if public and permitted, and relationship among parent/brand/branch. Do not infer corporate ownership from a similar name.
3. **Confirm a real location/service area.** Capture an actual facility address or a service city/area explicitly listed. Keep fields null or `not_stated` when absent. Do not derive a private person's address, invent coordinates, or turn national marketing language into local coverage.
4. **Create a separate service offer.** Use the taxonomy and an exact source-backed service label. Confirm setting (`at_facility`, `home_visit`, `remote`, `residential`, or `community`) and whether the offer is current. A service is not available at home merely because the provider is a home-health company.
5. **Capture business contact and official action links.** Use the source’s public organizational contact or booking URL. Confirm each link resolves to the official provider and do not claim real-time booking or availability unless stated and current.
6. **Verify regulated claims.** Check a named nurse with the relevant State/UT Nursing Council; check RCI-regulated professionals in the current RCI register; use HPR/other applicable statutory register as relevant. Keep registration evidence separate from the provider’s own claim and service availability.
7. **Review licence/privacy.** Confirm permission for each data source/field and public display. For personal data, confirm lawful basis/consent, minimization, access, retention, correction/removal process and privacy review. Do not collect patient data or identity documents.
8. **Attach evidence at claim level.** Store exact URL, date, method, source claim, status, verifier and note. Avoid copied paragraphs, photos, ratings, costs or review data without clear permission and a defined need.
9. **Deduplicate.** Compare official IDs, legal entity, brand/domain, physical address and source IDs. Resolve parent/brand/branch relationships; retain multiple legitimate location/service rows. Record merge decisions and never delete a valid service row solely due to repeated name.
10. **Run validation and review.** Apply required-field, source, geography, link, coordinate, postal, duplicate, verification, licence and freshness checks described below. A second reviewer signs off before a row is marked verified.
11. **Publish only approved facts.** Verified results show exact service/location scope and a source/last-checked date, link to official provider contact, disclose “availability to be confirmed with provider,” and avoid clinical endorsement. Unverified items remain internal or are clearly not presented as verified.
12. **Refresh or withdraw.** Set a review date by fact volatility. Reconfirm service, location, phone, hours and home-visit status periodically and after reports. Expire stale claims, suspend disputed records, and honor corrections/removal requests.

## 5. Verification levels and evidence standard

- `unverified`: candidate/source lead only; not for verified result display.
- `source_checked`: a public official page or registry entry was reviewed, but identity/service/active status has not been independently confirmed.
- `independently_verified`: the specific organization identity, service, location, contact and relevant credential facts were checked against authoritative evidence or directly confirmed; permission/privacy review is complete; evidence is still in its freshness window.
- `expired`: claim is stale or cannot be reconfirmed; suppress time-sensitive details.
- `disputed`: source conflict, provider challenge or material complaint unresolved; withhold disputed claims.
- `withdrawn`: provider/source withdrew permission or requested removal; remove from discovery, retaining only the minimum allowed audit record.

Status is claim-specific: a verified organization may have an unverified physiotherapy service, address, home-visit area or opening status. Do not promote the whole record because one identifier was checked. Keep availability separate from verification. Absence of a service statement is `not_stated`, not `No`.

## 6. Duplicate handling

- Preferred match keys: public source registry ID, verified legal entity identifier, exact official domain, and facility/site identifier, subject to reuse permissions.
- Compare organization identity separately from `brand_name`, site address and service. The same name may be independent entities; the same organization may use multiple brands.
- HCAH/Nightingales relationship and other parent/brand relationships must be checked from reliable evidence before deciding whether to merge or associate entities.
- One organization operating at multiple addresses has one organization identity with multiple location IDs. Each service at each location/area is a distinct offer row.
- Do not deduplicate by provider name, phone alone, similarity score alone or shared service label. Send ambiguous matches to manual review.
- Retain source records, merge/split decisions and lineage. Preserve raw names and normalized values side by side.

## 7. Geographic coverage and location checks

All India means all States and Union Territories are in the acquisition target, not that every district/provider is represented. Maintain a State/UT × district × service-category coverage ledger with `verified_count`, `candidate_count`, `not_yet_researched`, source and latest research date.

- Standardize state/district names only against an authoritative geography source while preserving source spelling.
- Preserve postal codes as strings; format validity does not prove geographic correctness.
- Validate latitude/longitude globally and against approximate India boundaries, then check that a facility coordinate agrees with its actual address/state. Keep point provenance and uncertainty.
- Company service areas should be listed per service and city/district only when explicitly confirmed. Do not assign coverage radius or interpolate between cities.
- Do not store or pinpoint an individual caregiver/professional's private residence. Use a public clinic or a coarse service area only where appropriate and consented.

## 8. Data quality and audit checks

Before a row can be approved:

- Required provider, service, location, source and status fields are present; unknown values remain null or explicit not-stated codes.
- Source is official/authoritative for the claim; link and record ID are preserved.
- Name, organization/brand, provider type and source status are coherent.
- Service category is explicit; home-visit/remote/residential modes are independently evidenced.
- State, district, city, PIN and coordinates are internally plausible and source-linked.
- Business contact and booking links are official, reachable and current; do not infer contact details from search snippets.
- Qualifications and registrations are checked against the appropriate regulator; training credentials and clinical licences are distinct.
- Current status and verification dates meet freshness policy; source permission/licence is recorded.
- Repeated provider names are retained until identity resolution; exact duplicates are reviewed at the correct provider-service-location grain.
- No synthetic data, fake ratings, invented prices, generated availability, patient data, copied protected media or unsupported claims are present.
- A second reviewer checks any record with conflicting sources, missing key fields, personal data, professional credentials, residence status or a patient safety concern.

## 9. Patient/provider matching requirements and boundaries

The provider dataset stores provider facts only. Patient location and health/logistics preferences are query inputs and must not be copied into the provider directory. If user data is persisted for accounts or matching, it requires a separate privacy and security design, purpose limitation, consent/appropriate lawful basis, access control and retention policy.

### Evidence-based matching filters

1. **Patient location:** compare patient-selected location with verified facility location or explicitly verified service coverage. Do not use an inferred radius or stale city list.
2. **Required service:** require an exact or approved taxonomy mapping supported by evidence. `home nursing` must match explicit home nursing; facility nursing or a hospital listing is not enough.
3. **Home visits:** require `home_visits_available=yes` and a confirmed covered location for home-visit requests. `not_stated` does not match.
4. **Injury/rehabilitation requirements:** use the patient-selected service need to filter only to explicit service labels/specializations and verified relevant qualifications. Do not infer that a provider treats a condition from a generic “rehabilitation” label or make clinical suitability/treatment recommendations. When a user is unsure what service to select, route to an appropriate clinician/official care channel rather than predicting need.
5. **Mobility limitations:** use only declared service/logistics facts such as wheelchair access, transfer support or at-home mode when confirmed for that location. Do not infer capabilities from a provider category.
6. **Patient weight:** do not use weight to judge clinical suitability or rank providers. Use it only if the user chooses a relevant care-logistics need and the provider explicitly publishes a safe supported threshold/equipment requirement; otherwise leave it out of matching and direct the user to confirm privately with the provider.
7. **Required qualifications:** require an appropriate verified credential for regulated care. A company’s general “trained team” statement does not verify every clinician. Caregiver training is not equivalent to nursing/clinical licensure.
8. **Provider coverage:** require a location/service-area match for the particular service and delivery mode.
9. **Verified contact or booking link:** include only current official channels. Availability is a separate time-sensitive fact and should be confirmed with the provider.

### Results behavior

A matching result is a discovery shortlist based on explicit service, geography, mode and credential facts; it is not a medical recommendation, diagnosis, quality score, or assurance of acceptance/availability. Explain the facts that matched, show evidence date and official contact link, and state unknowns clearly. Do not score providers on synthetic ratings, fabricated cost, or unverified experience.

## 10. Privacy and patient safety

- Prioritize organization/facility and business details. Individual listings remain out of this organization-service pilot unless separately approved.
- Do not collect patient diagnoses, injury narratives, weights, mobility details, ABHA/Aadhaar, medical records, identity documents, private address or private contact as part of provider research.
- Do not reuse caregiver/professional personal profiles solely because they are publicly visible. Obtain required consent, source permission and legal review; provide correction/removal handling.
- Do not expose patient matching inputs to providers until a user deliberately contacts a provider through an official channel and consents to sharing.
- Avoid clinical ranking or treatment selection. Keep scope to discovery and logistical filters; direct medical decisions to qualified clinicians.

## 11. Pilot CSV and approval gate

`data/templates/provider_pilot_template.csv` is a separate, empty CSV for organization-service-location records. Its row grain is not person or employment data. It includes source/evidence, status, permission, location, service mode and matching facts with unknown represented explicitly. It must remain empty until genuine source records are permitted and verified. The target is eventually 50–100 rows; the pilot may be smaller if source permissions or evidence do not support 50 qualifying rows.

Before any real collection begins, approve the chosen source(s), use method, licence/permission, privacy protocol and pilot geographies. This preparation task has not called APIs, scraped sites, downloaded provider datasets, installed packages, or populated the CSV.

## 12. Source references

Use the source-by-source findings and citations in [`provider_source_audit.md`](provider_source_audit.md). Recheck each official page and current access/terms before collection. In particular, ABDM API documentation is ecosystem integration information, not automatic permission; public website visibility is not a general data-reuse licence; nursing NRTS enrollment does not replace State/UT Council licensure; and SHATAYU’s own disclaimer requires independent checks.
