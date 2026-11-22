# CareRoute provider service taxonomy

**Version:** 1.0 (planning taxonomy)  
**Scope:** India-wide discovery of real organisations, facilities and consenting professionals offering existing healthcare, home-care, elderly-care or related support. A taxonomy label is a classification only; it does not establish that a provider offers the service or is qualified to do so.

## Service categories

| Category code | Category | Example subcategories | Provider types commonly associated | Evidence needed before displaying a service |
|---|---|---|---|---|
| NUR | Nursing | Skilled nursing visits; post-operative nursing; wound care; medication administration where within scope; catheter/stoma care; monitoring; bedside nursing | Home healthcare company; hospital/facility; nursing agency; individual registered nurse | Provider-published service details; for individuals, current council registration and qualification where applicable; locality and visit availability verified separately |
| PHY | Physiotherapy and rehabilitation | Musculoskeletal; neurological; post-surgical; geriatric; respiratory; mobility/gait; home physiotherapy; clinic-based physiotherapy | Clinic/rehabilitation facility; home healthcare company; individual physiotherapist | Explicit service listing and care setting; verify credentials with relevant registration/qualification source when available; no clinical suitability inference |
| ELD | Elderly and geriatric care | Geriatric assessment; elder-care coordination; dementia support; companionship; respite; post-hospital support; caregiver support | Elder-care organisation; home-care company; residential provider; individual geriatric caregiver | Explicit elder-care offer, coverage, and whether clinical or non-clinical; time-sensitive service status |
| HHC | Home healthcare (delivery setting) | Home nursing; doctor visit; diagnostics/sample collection; home rehabilitation; home palliative support; equipment delivery; post-discharge services | Home healthcare company; hospital/home-care unit; clinic; individual professional acting through an established practice | Explicit home-visit or home-delivery statement plus service and covered locality. Treat this as a cross-cutting setting tag, not a claim that all listed services are available at home |
| PER | Personal care and daily-living support | Bathing/dressing assistance; feeding support; mobility transfers; toileting; companionship; household/personal assistance | Home-care organisation; elder-care organisation; geriatric caregiver; residential provider | Explicit task list, caregiver role, service hours and location; distinguish non-clinical personal care from nursing |
| MED | Medical support and allied services | Physician/medical visits; diagnostics; medication support; medical equipment; post-discharge coordination; chronic-care support; emergency referral coordination | Hospital/facility; home healthcare company; clinic/lab; registered individual professional | Exact service and setting, scope, qualifications or facility authorization as applicable; do not represent equipment or coordination as clinical treatment |
| DIS | Disability support | Disability rehabilitation; occupational therapy; speech and language therapy; assistive technology; mobility/orientation support; special education; community-based rehabilitation | Rehabilitation centre; disability support organisation; residential provider; registered rehabilitation professional | Service-specific evidence; verify RCI registration for regulated RCI professional categories; accessible service details and support setting |
| PAL | Palliative and end-of-life care | Symptom support; home palliative visits; hospice/palliative services; family and caregiver support; respite | Hospital/palliative unit; hospice; home healthcare company; residential provider; qualified care team | Explicit palliative service and delivery setting; provider evidence, referral requirements and geographic availability; do not imply emergency care |
| RES | Residential and supported living | Senior living; assisted living; care home; long-term residential care; short-stay/respite stay; dementia/memory care; rehabilitation stay | Residential care provider; assisted-living or senior-living operator; hospital step-down facility | Physical location, admission/service model, support level, contact and current operational status verified directly; do not conflate with home care |
| MHS | Mental health support | Psychiatry; clinical psychology; counselling; psychosocial support; dementia-related support; tele-mental health; community mental health | Mental health facility; hospital; clinic; telehealth organisation; registered individual professional; public helpline/service | Exact service and scope, practitioner qualifications/registration as applicable, mode (in-person/remote), service area and current access route; helplines are not provider listings unless the directory explicitly includes services |

## Provider entity classes (separate from service categories)

Use one primary `provider_type` for the entity being listed. Do not infer it from a service label.

1. **Healthcare facility** — hospital, clinic, rehabilitation centre, diagnostic facility, public health facility or other fixed care institution. A facility registry record establishes identity/location only to the extent stated by that registry; it does not prove all services, current opening or home visits.
2. **Home healthcare company** — an organisation that coordinates or directly provides healthcare in a patient's home. Record the organisation and its explicit service/location claims. Do not list its workforce as employees or imply CareRoute recruits them.
3. **Individual professional** — a named, consenting professional offering an existing service/practice, such as a nurse, physiotherapist, doctor, psychologist or RCI-regulated rehabilitation professional. Verify credentials and public listing permission independently. Do not collect Aadhaar, private contact details or unnecessary identity data.
4. **Geriatric caregiver** — a person offering elderly-care support, including non-clinical daily-living assistance. Keep this distinct from a registered nurse or other licensed professional. SHATAYU and similar directories can be candidates for source verification, subject to their terms and consent requirements.
5. **Residential care provider** — an operator of a named senior residence, assisted-living centre, care home, hospice or similar place where a person stays. Store each physical location as a distinct service-location record where appropriate.

An organisation can operate multiple facilities or service areas. Model its identity separately from each location and each service offer. A multi-service company remains a company record with several service-location rows, not several invented provider identities.

## Controlled values and interpretation

- Service category codes are the codes above; permit multiple categories per provider-service listing only where source evidence supports each one.
- Delivery mode: `at_facility`, `home_visit`, `remote`, `residential`, `community`, `not_stated`.
- Listing/verification status: `unverified`, `source_checked`, `independently_verified`, `expired`, `disputed`, `withdrawn`.
- Claim state: `verified_available`, `verified_unavailable`, `not_stated`, `not_checked`, `expired`. Missing information must remain `not_stated` or null, never be converted to `No` or a positive claim.
- Keep clinical qualifications, organisational identity, service scope, service location, home-visit availability and operational status as separate facts with their own evidence and dates.
