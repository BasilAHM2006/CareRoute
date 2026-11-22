# CareRoute provider data collection plan

**Phase:** 3 — planning only  
**Prepared:** 2026-11-21  
**Scope:** All India; existing real-world healthcare, home-care and elderly-care organisations, services, facilities and consenting professionals. No website scraping, API calls, bulk data downloads, or provider records were collected for this planning task.

## Purpose and guardrails

CareRoute is a provider discovery and matching platform. It should identify real organisations and existing service offers and help users compare verifiable facts and contact the provider. It is not an employer, staffing exchange or job marketplace. Individual professionals and geriatric caregivers are separate entity types; list them only as existing consenting service providers where lawful and safe, not as people seeking work. Do not invent names, contacts, qualifications, prices, availability, home visits, capacity, credentials, reviews or service coverage. Synthetic demonstration rows remain isolated and must never be merged, relabelled or presented as real providers.

The existing public healthcare Parquet may be used later as a facility-discovery seed after review of its provenance, terms, quality and current status. It mostly describes public facilities and has no demonstrated home-visit or clinical-service availability. It must not be used to infer provider services. Existing processed data and the synthetic CSV were inspected read-only and left unchanged.

## Taxonomy and entity separation

Service categories and definitions are in [`../docs/provider_service_taxonomy.md`](../docs/provider_service_taxonomy.md). Use service category separately from provider entity type. Keep these groups distinct in collection, verification, UI and reporting:

1. **Healthcare facilities:** hospitals, clinics, rehabilitation centres, diagnostic facilities and other fixed facilities. Registry inclusion supports identity/registry status only; verify current service and address claims.
2. **Home healthcare companies:** organisations delivering or coordinating named services at home. Store official company identity, explicit service/city coverage and mode of delivery. Service pages are not proof that every city or every service is currently available.
3. **Individual professionals:** consenting nurses, physiotherapists, physicians, psychologists and other professionals with an existing practice/service. Verify applicable council registration/qualification. Do not expose private residence or personal contact data.
4. **Geriatric caregivers:** caregiving personnel and non-clinical personal care roles. Do not call them nurses unless their nursing credentials are verified. SHATAYU is a possible official directory source, but its personal-profile model and disclaimers require consent, privacy and non-marketplace policy review before use.
5. **Residential care providers:** senior residences, assisted living, care homes, hospices and other stays. Create one location record per residence and verify operating/admission status; do not confuse a residence with home care.

An organisation can have multiple locations and service offers. Keep the stable provider identity, location and provider-service offer as related records; use the proposed record grain in [`../docs/provider_data_dictionary.md`](../docs/provider_data_dictionary.md).

## Candidate source inventory

The CSV inventory at [`../data/raw/provider_source_inventory.csv`](../data/raw/provider_source_inventory.csv) contains candidate sources, their official URLs, expected data, access/reuse caveats, verification approach and collection status. Every row is `candidate_not_collected`; `last_checked` means the official source candidate was researched for this plan, not that provider records were refreshed or validated.

Initial source tiers:

- **Identity and credential authorities:** ABDM Health Facility Registry (HFR); ABDM Healthcare Professionals Registry (HPR); Indian Nursing Council and the relevant State/UT Nursing Council; Rehabilitation Council of India’s Central Rehabilitation Register for its regulated categories.
- **Caregiver directory candidate:** SHATAYU, the Government of India geriatric caregiver dashboard. It is a person-level directory, with official warnings that candidates supply information and that users independently verify background/suitability. Treat it as a candidate source, not a guarantee.
- **Provider-controlled organisation sources:** Portea, Apollo HomeCare, HCAH, Nightingales, Antara Senior Care and Emoha. These help establish the organisation’s own current service and location claims; they do not replace credential checks or independent confirmation.
- **Mental-health public service resource:** Tele-MANAS may be represented separately as a national service/helpline resource, not as a specific private provider or emergency response service.

No source in the inventory has been approved for automated scraping, bulk copying or republication. Confirm exact portal terms, licence, API/bulk access rules, data-protection responsibilities and necessary permissions before collection. Public access is not by itself a reuse license.

## Collection strategy and source priority

1. **Define claim-level questions first.** For every prospective listing, identify which facts users need: provider identity, service category, location, home visit/remote/residential mode, business contact and current access route. Do not collect irrelevant personal data.
2. **Start with official registers for identity and professional credentials.** Use HFR for facility identity and stated attributes; HPR and relevant councils for professional identity/registration; RCI/CRR only for its regulated professional classes. These sources do not necessarily verify service availability, quality, capacity or home visits.
3. **Verify organisation services with the organisation.** Use official service pages and direct provider confirmation for service scope, city, visit model, contact, operating status and booking routes. Record the exact URL, date, method and what each source supports.
4. **Use official caregiver directories cautiously.** For SHATAYU or equivalent person-level source, verify listing status and credentials as applicable, obtain/confirm permission for CareRoute republication, and minimize personal data. Do not import profile details wholesale.
5. **Use public registries and government datasets only within their terms.** The existing facility dataset and any future source data must retain source IDs, attributions, retrieval dates and license notes. An open facility registry record remains only a discovery seed until its current existence/location/service is checked.
6. **Do not treat aggregators, search snippets, social profiles, user submissions or marketing claims as proof.** They may point to a lead; verify the facts through official sources. Label any permitted provisional lead as unverified and do not present it in verified results.
7. **Collect in batches by state/UT and district, then audit coverage.** Track source coverage separately from provider coverage. Report states/districts with no sourced listings as “not yet collected,” never as having no providers.

## Verification process

For each candidate provider/location/service:

1. Confirm that the source is official or an authoritative regulator/registry and preserve the specific source URL/record identifier.
2. Confirm real-world identity and operating status. Resolve brand/legal entity carefully, especially related brands and local franchise/operators.
3. Confirm each service separately, including its exact category and delivery mode. Verify home visit, remote access, residential stay, area served, availability, opening hours, price and capacity only if the source explicitly states them and they are current. Omit unsupported claims.
4. For regulated individuals, verify the relevant qualification, council/register, registration number/status and validity with the appropriate authority. Do not use a generic company claim to verify an individual. For geriatric caregivers, distinguish non-clinical caregiver training from professional clinical credentials.
5. Confirm the public contact and booking link via provider-controlled channels. Do not expose personal mobile/email/address unless it is explicitly published for service contact and lawful to reuse.
6. Record claim-level evidence, method, source attribution, date checked, status and next review date. Store only a short factual evidence note; do not copy large website text or images.
7. Assign `unverified`, `source_checked`, `independently_verified`, `expired`, `disputed` or `withdrawn` according to the data dictionary. A checked source page alone is not independent verification. Only records whose identity and user-facing claims satisfy the agreed verification standard should appear as verified.
8. Recheck time-sensitive facts on a defined schedule and when users/provider owners report a change. Expire or suppress stale service, contact, location, operating and availability claims until refreshed.

## Duplicate handling

- Use official registry IDs or verified legal identifiers as preferred organization/facility keys where permitted; preserve the source key and source name.
- Match organizations using legal name, brand, official domain and addresses, but do not merge brands or branches solely because names look similar.
- Model branches/residences as separate locations attached to a common provider organization when evidence supports that relationship.
- Model each distinct service and delivery location as a separate provider-service-location record. Repeated provider names are not sufficient evidence of duplicates.
- For individuals, use only public/consented identifiers and registry evidence; do not use phone number alone as a universal key. Avoid storing duplicate personal profiles across registries.
- Retain merge/split decisions and source lineage. Never silently delete source rows; preserve the record or audit lineage as retention and privacy rules permit.

## Geographic coverage

The target is all States and Union Territories of India. Coverage is an acquisition goal, not a claim that the directory is exhaustive. Track counts by state/UT, district, service category, provider type and source, as well as areas with no research yet. Use official State/UT and district reference lists for canonical spelling, retaining source spellings. Validate coordinates and PIN codes using authoritative references; retain coordinate provenance and uncertainty. Do not geocode private addresses or derive exact coordinates for people. For companies with distributed coverage, record each explicitly confirmed service city/area, not a national label unless national availability is evidenced for that service.

## Data quality checks

Before accepting or publishing a row, check:

- required identity and source fields; URL validity and source authority;
- permitted, non-empty service category and provider type;
- source-backed service name, delivery mode and status;
- state/district/city consistency and location plausibility;
- PIN format plus authoritative geographic match where feasible;
- coordinate ranges, India bounds and match to the actual facility/location;
- business phone/email syntax and whether contact is actually public;
- professional qualification/registration against issuing authority when applicable;
- dates, freshness window, source availability and licence/permission;
- duplicates at provider, location and service grains;
- missing values remain missing/unknown, never assumed unavailable/available;
- conflicting sources and service claims flagged for resolution;
- no synthetic demo records, patient data, fabricated details or unsupported clinical claims.

Track missingness by field and source, not just as a single score. A listing with missing phone or home-visit status may still be usable for limited facility discovery if its verified facts are clearly scoped; it must not receive inferred contact or service claims.

## Privacy, consent and safety

- Prefer organisation/facility facts and business contact channels over information about natural persons.
- For individual professionals and caregivers, document consent or another valid lawful basis for directory inclusion, explain purpose and public display, offer correction/removal routes, and collect only necessary professional facts.
- Do not collect Aadhaar, identity-document images/numbers, patient records, health conditions, personal home addresses, private phone numbers, or sensitive details from registration workflows.
- Avoid reproducing personal data just because it appears on a public page. Review applicable Indian privacy/data-protection requirements and each source's terms before ingestion and publication.
- Apply access control, retention/deletion rules, audit logs and breach handling to any non-public source material. Keep source evidence for the minimum justified period.
- Do not make automated clinical suitability judgments. Matching should filter on declared, verified service/location/logistics and show evidence, uncertainty and official contact paths.
- A directory listing is not a clinical endorsement, credential guarantee beyond the specific check, or confirmation that a provider is available at the time of contact.

## Verified versus unverified listings

| State | Meaning | Display treatment |
|---|---|---|
| `unverified` | Candidate identified; substantive claims not checked | Do not include in verified/provider results. Use only in internal research queue. |
| `source_checked` | Source page reviewed, without independent confirmation of identity/current claims | Clearly label as source-checked/unconfirmed if shown at all; avoid availability or credential guarantees. |
| `independently_verified` | Identity and specific published claims checked with authoritative evidence, valid consent/reuse basis, and within freshness window | May be displayed with claim-level evidence/date and clear link to official provider channel. |
| `expired` | Verification became stale or current status could not be reconfirmed | Suppress time-sensitive claims and mark for review. |
| `disputed` | Credible source conflict or complaint unresolved | Hide or withhold disputed claims until resolved. |
| `withdrawn` | Provider/source withdrew the listing or consent/permission ended | Remove from discovery; retain only minimal permitted audit record. |

Unknown fields should display as “not stated” or be omitted; never turn them into factual negatives. Keep the verification state separate from provider service status.

## Outputs and implementation boundary

Planning artifacts created in this phase are the taxonomy, source inventory, proposed dictionary, empty CSV template and this plan. The source inventory contains candidate sources, not collected provider records. The provider template contains only a header row. No API calls, website scraping, installs, provider-record collection, or dataset changes are part of this phase. Before actual collection, review candidate source terms/licences, approve the verification and privacy protocol, and choose a small pilot geography/source set while maintaining an All-India coverage ledger.

## Research notes and official references

Sources were reviewed on **2026-11-21** for planning; candidate pages can change. No underlying provider/person records were inspected or copied.

- [ABDM Health Facility Registry registration information](https://facility.abdm.gov.in/) and [ABDM HFR/HPR registry overview via NHA/ABDM material](https://abdm.gov.in/).
- [ABDM HPR portal](https://hpr.abdm.gov.in/); [National Health Authority release on HFR and HPR](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2288848&lang=1&reg=1). HPR/HFR are registry sources, not proof of home service availability.
- [Indian Nursing Council state council directory](https://indiannursingcouncil.org/statenursings).
- [SHATAYU official dashboard](https://shatayu.dosje.gov.in/) and [official disclaimer/dashboard information](https://shatayu.dosje.gov.in/about). It cautions that candidate-provided information needs independent checks.
- [Portea official service pages](https://www.portea.com/); [Apollo HomeCare](https://www.apollohomecare.com/); [HCAH service pages](https://www.hcah.in/all-services/); [Nightingales](https://www.nightingales.in/); [Antara Senior Care](https://www.antaraseniorcare.com/); [Emoha](https://emoha.com/).
- [Rehabilitation Council of India Central Rehabilitation Register search](https://rciregistration.nic.in/rehabcouncil/newsearchpage.jsp) and [RCI registration guidance](https://rehabcouncil.nic.in/norms-guidelines/).
- [MoHFW National Mental Health Programme / Tele-MANAS information](https://www.dghs.mohfw.gov.in/national-mental-health-programme.php).

These links establish why each candidate merits research; they do not grant CareRoute permission to copy listings or certify the accuracy/current status of every record.
