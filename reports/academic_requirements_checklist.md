# Academic requirements checklist — CareRoute

## How to read this checklist

CareRoute is the student's selected project idea. The college handout's general ten-step workflow is the academic framework. The separate Student Academic Performance Analysis example illustrates one possible project and is **not** treated as a mandatory dataset or target. CareRoute-specific analytical choices below are proposed adaptations; seek lecturer approval where noted. Nothing here claims that synthetic demo data are real provider evidence.

The supplied materials included a list of 15 suggested project ideas. They are: (1) Student Performance Analysis and Prediction; (2) Healthcare Risk Analysis and Disease Prediction; (3) Loan Approval and Credit Risk Prediction; (4) Employee Attrition Analysis and Prediction; (5) House Price Prediction Using Statistical Analysis; (6) Retail Sales Analysis and Sales Prediction; (7) Weather Data Analysis and Temperature Prediction; (8) E-Commerce Customer Purchase Behaviour Analysis; (9) Customer Churn Analysis and Prediction; (10) Traffic Accident Data Analysis; (11) Online Shopping Behaviour Analysis; (12) Air Quality Analysis and Prediction; (13) Insurance Claim Analysis and Prediction; (14) Student Placement Analysis and Prediction; (15) Electricity Consumption Analysis and Prediction. CareRoute is the selected project, rather than the student example. “Healthcare Risk Analysis and Disease Prediction” is not the CareRoute objective: CareRoute discovers services and does not diagnose or judge clinical suitability.

## General 10-step implementation workflow

| # | Original workflow requirement | Proposed CareRoute implementation | Status / approval note |
|---:|---|---|---|
| 1 | Define the problem statement and project objectives. | Define the user need as finding existing providers by required service, location, home-visit logistics and other verified service attributes. State that CareRoute is not a healthcare agency and does not make medical decisions. | Core scope; obtain lecturer acceptance of project framing. |
| 2 | Collect and understand the dataset (500–1,000+ records). | The current file has 1,000 rows and meets the scale only. It is synthetic/unverified. Collect a real, source-documented provider-service directory; confirm with lecturer whether this and/or a separate analytic dataset meets the assignment. | Authenticity, not row count, is the blocker. |
| 3 | Clean and preprocess the data. | Preserve source records; standardize a derived copy; validate types, controlled terms, geography, provenance, duplicates and missingness. | Applicable after sourcing real data; do not modify the original CSV. |
| 4 | Perform descriptive statistical analysis. | Summarize verified listing coverage: services/providers by city, provider types, home-visit availability and verified price distributions if comparable quotes exist. | Current file supports demonstration only; substantive results need actual sourced listings. |
| 5 | Apply probability concepts and hypothesis testing (hypothesis test, conditional probability, Bayes’ theorem). | Define nonclinical events such as verified home-visit availability by service/city and compare groups only with an appropriate sampling frame. Bayes can update a clearly defined listing/logistics probability, not medical risk. LLN can be illustrated via repeated samples. | Lecturer approval recommended for the adapted events, sampling frame and inferential interpretation. Synthetic values cannot support population claims. |
| 6 | Perform correlation and regression analysis (correlation matrix and simple linear regression). | Explore relationships among sourced numeric provider-service measures only when meaningful. Regression requires a defensible outcome such as comparable verified quoted cost; define units, date, service type and predictors. | Current dataset has no trustworthy target. Lecturer approval required for adapted target/features; no forced regression. |
| 7 | Implement mathematical operations using NumPy (matrix operations, regression calculations, gradient descent). | Demonstrate vectors/matrices and regression calculations using the approved analysis dataset. | NumPy is explicitly named. Basic matrix arithmetic can use demo data, but regression/gradient descent needs a valid outcome. |
| 8 | Develop and optimize the model. | If approved and supported by sourced labeled observations, build an academic model for a bounded operational quantity (for example quote-cost estimation); do not rank clinical suitability. | Lecturer approval and valid dataset/target required. Not supported by current CSV. |
| 9 | Evaluate the model using suitable metrics (MAE, MSE, RMSE, R², and residual analysis). | Evaluate only after held-out actual outcomes and predictions exist. State metric units and residual interpretation for the chosen numeric target. | Current CSV cannot support model evaluation. Use these exact metrics if a regression model is approved. |
| 10 | Prepare the final project report and presentation. | Document objectives, provenance, methods, results, limitations, safety boundary and provider-source verification. Present synthetic data only as demo data. | Required final deliverables after approved analysis. |

## Mathematical/statistical techniques mapped to CareRoute

### Descriptive and inferential statistics

- **Techniques from the example:** mean, median, mode; variance, standard deviation; distributions; sampling; hypothesis tests comparing groups.
- **CareRoute adaptation:** describe real, verified directory composition. For numeric fields, consider comparable quoted service costs or verified provider coverage measures. Compare service/provider/location groups only when sampling and measurement are defensible.
- **Approval/limits:** mean/variance of `estimated_hourly_cost_inr_demo` from the current CSV are statistics of generated numbers, not market estimates. Define null/alternative hypotheses, population, sampling, test assumptions and significance threshold with lecturer; the handout does not prescribe these.

### Probability, conditional probability, Bayes’ theorem, law of large numbers

- The student example uses “score above 80” and “attendance above 75%”; those exact events do not apply to CareRoute and are not mandatory.
- Possible CareRoute events: a verified provider offers home visits; a listing covers a selected city; or a provider offers a service given a service category. Conditional probabilities require a well-defined denominator and verified source data.
- Bayes’ theorem may illustrate updating the probability that a directory listing meets a logistical attribute given observed metadata. Do not frame it as a clinical diagnosis or suitability assessment.
- Law of large numbers can be shown with repeated samples from a defined dataset. A synthetic sample illustrates arithmetic only, not convergence to actual provider-market truth.
- Lecturer approval recommended before claiming inferential meaning from these adapted events.

### Correlation and regression

- The example specifies Pearson and Spearman correlation and a correlation matrix. For CareRoute, use them only on meaningful numeric variables and exclude IDs. Correlation among generated fields may reflect how records were constructed.
- The example's student variables (`Attendance`, `Study_Hours`, `Assignment_Score`, `Internal_Marks`, `Previous_Semester_Marks`, `Final_Marks`) are illustrative and are not CareRoute requirements.
- For provider analysis, a possible regression response is a **verified comparable quoted cost**. Candidate predictors might include service category, visit type/duration, location and date. This requires enough authentic, comparable observations, clear units and treatment of time/location effects. Do not use a demo estimate as target or infer clinical quality/suitability.
- An alternative is no prediction model: perform descriptive provider-service analysis if no defensible target exists. The general workflow should not force a misleading model.
- Lecturer approval required for revised outcome, predictors, model purpose and claims.

### Linear algebra, calculus, optimization

- Represent approved numeric observations/features as vectors/matrices; demonstrate matrix addition, multiplication and dot products. Explain regression calculations through matrix operations when a valid target is present.
- Define the cost function for an approved regression target, derive its derivative, and demonstrate gradient descent/parameter changes. The handout names these techniques but does not prescribe a cost function, learning rate or convergence rule; document choices and seek approval.
- Current numeric synthetic columns can demonstrate arithmetic only. They do not justify a real-world fitted prediction model.

### Model evaluation and residuals

- Preserve the named metrics: **MAE, MSE, RMSE, R²**, actual-versus-predicted comparison, residual plots and over/underestimation analysis.
- Apply only if a valid numerical outcome exists and test data are held out. State the target units. Residuals refer to prediction error for that target, not healthcare safety or clinical suitability.
- Current file has no trustworthy observed target, so metrics cannot validly evaluate a model.

## Student-performance example: retained as example, not a CareRoute requirement

The document's separate example proposes 500–1,000 student records with `Student_ID`, `Gender`, `Attendance`, `Study_Hours`, `Assignment_Score`, `Internal_Marks`, `Previous_Semester_Marks`, `Sleep_Hours`, `Extracurricular_Activities` and `Final_Marks`; it demonstrates marks thresholds, attendance threshold, and regression predicting `Final_Marks`. These student-specific records, variables and questions are **not required for the selected CareRoute project**. They should not be silently transplanted into a provider directory. The relevant requirements adopted here are the general workflow and appropriately approved mathematical methods.

## Dataset findings relevant to this checklist

- Current CSV: **1,000 rows × 20 columns**; meets record-count scale.
- 0 blank cells; 0 exact duplicate rows; 0 duplicate IDs; 0 repeated provider names.
- Numeric fields: `experience_years`, `rating_demo`, `estimated_hourly_cost_inr_demo`, `service_area_radius_km_demo`, `number_of_services_demo`.
- All records are marked `SYNTHETIC_DEMO_ONLY`; source says generated synthetic demonstration data, and verification says synthetic/not verified.
- No real provider identities, source URLs, official contacts/booking links, verification dates, patient outcomes, booking outcomes, or clinically validated labels.
- Therefore it is suitable as a synthetic schema/UI or arithmetic exercise only, not factual provider discovery, market inference, or a real predictive model.

## Data requirements and next academic decision

### Product directory (Dataset A)

Use real provider-service-location records with Provider ID, provider name, provider type, service, specialization, city, district, state, home-visit availability, service coverage, official website, contact, booking link, data source, verification date and verification status. Keep evidence/source URL and last-checked date. Verify each claim; use `unknown`/`unverified` honestly. Match service and logistics only; allow provider channels to handle clinical questions.

### Analysis dataset (Dataset B, only if needed)

If lecturer requires regression/calculus/evaluation beyond descriptive directory analysis, obtain a separate approved dataset with a coherent, measured target. One possible CareRoute operations question is estimation of a comparable quoted service price from verified service/visit/location/date attributes. Define sampling frame, units, collection dates, missingness and source. Alternatively use an instructor-approved, relevant public dataset. Keep Dataset B analytically separate from Dataset A unless a justified join is designed. Do not fabricate a target or mix student records with providers.

## Originality, provenance and safety controls

- Never represent synthetic provider names, ratings, costs, availability, experience, geography or service capabilities as genuine.
- Do not invent official links or booking channels.
- Keep raw source unchanged; store source and verification metadata in derived data.
- Do not use patient age, weight, injuries or surgeries to make clinical suitability decisions. Any patient-facing service preference is a logistical filter, not medical advice.
- Keep the project a discovery/referral platform, not a provider employer or care agency.
