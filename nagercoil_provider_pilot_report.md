# Nagercoil provider pilot report

**Verification date supplied:** 2026-11-21  
**Evidence method supplied:** Direct phone contact with each provider; the user reports completing the calls.  
**Evidence status:** Provider-reported claims. No regulator registration, facility licence, individual qualification, or service-specific documentation was supplied or checked for this file.

## Summary

The pilot contains **four hospital candidates** and **16 organization-service-location rows**: four explicitly requested service claims per hospital. The row grain follows the provider data workflow and keeps nursing, home nursing, physiotherapy, and home physiotherapy as separate service/mode claims.

| Hospital | Nursing | Home nursing | Physiotherapy | Home physiotherapy |
|---|---|---|---|---|
| Dr. Jeyasekharan Medical Trust | Yes | No | Yes | No |
| Be Well Hospitals | Yes | No | Yes | No |
| Bethesda Hospital | Yes | No | Yes | No |
| Calwin Hospitals | Yes | Yes | Yes | Yes |

**Calwin Hospitals is the only one of these four reporting all four services**, including both home nursing and home physiotherapy. “Yes” and “No” in this comparison reflect the provider-reported answers supplied by the user, not regulator-verified or independently documented claims.

## Source and evidence handling

- Each provider's supplied official URL is preserved in `official_website_url`, `official_service_url`, and `source_url`; those URLs were not independently visited or validated in this data-entry task.
- The phone numbers, addresses, and service statuses are preserved as supplied. Phone values remain strings.
- `source_id` is `USER-REPORTED-DIRECT-PHONE`, a task-level provenance key. It is not an entry in `data/raw/provider_source_inventory.csv`, which was left unchanged.
- `verification_status` is `source_checked`; `verification_method` states that direct phone contact was reported by the user and was not independently repeated by CareRoute. The service status is recorded as `verified_available` or `verified_unavailable` according to those provider reports. Evidence notes make the limits explicit.
- No regulator verification or individual professional qualifications were supplied. Qualification fields remain blank or `not_checked`; no credentials are inferred.
- Home-visit availability is set only for the home-nursing and home-physiotherapy rows. No home-visit coverage area was supplied, so it remains blank even for Calwin.
- Reuse permission for website content/data has not been established; `reuse_permission_status` remains `not_confirmed`.
- District was supplied only for Dr. Jeyasekharan Medical Trust and is left blank for the other three. No coordinates, operating hours, prices, capacity, or booking links were added.

## Remaining checks before public display

Confirm provider identity and each service claim from a saved source record or a repeatable direct confirmation; confirm current status and home-visit coverage for Calwin; check provider/site reuse terms; verify any professional qualifications separately if CareRoute later names clinicians. Keep the current records marked as provider-reported until the evidence standard is met. This file does not establish clinical suitability, quality, price, appointment availability, or endorsement.

## Output

- Data: `data/processed/nagercoil_verified_provider_pilot.csv` — 16 data rows, 59 columns.
- Existing 59-column template was read and left unchanged.
- No original or processed dataset, source inventory, prior report, or taxonomy/dictionary/workflow file was modified.
