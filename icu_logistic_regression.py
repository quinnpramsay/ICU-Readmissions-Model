from sklearn.linear_model import LogisticRegression # binary classification
from sklearn.model_selection import train_test_split # to train and test the model
from sklearn.preprocessing import StandardScaler # to scale everything to comparable values
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, roc_curve # Help test the model to see how good it is
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Access data using Google BigQuery.
from google.colab import auth
from google.cloud import bigquery

auth.authenticate_user()

#Access data set from google BQ
project_id='icu-readmissions-ai-project'
client = bigquery.Client(project=project_id)

# MIMIC-IV v3.1 dataset information
MIMIC_PROJECT = "physionet-data"
MIMIC_DATASET_HOSP = "mimiciv_3_1_hosp"
MIMIC_DATASET_ICU = "mimiciv_3_1_icu"

#query all data from MIMIC-IV dataset
query = f"""WITH icu_stays AS (
    SELECT
        icus.subject_id,
        icus.hadm_id,
        icus.stay_id,
        icus.intime,
        icus.outtime,
        icus.los as icu_los_days,
        icus.first_careunit,
        icus.last_careunit,
        LEAD(intime) OVER (PARTITION BY subject_id ORDER BY intime) as next_icu_intime,
        LEAD(stay_id) OVER (PARTITION BY subject_id ORDER BY intime) as next_stay_id
    FROM `{MIMIC_PROJECT}.{MIMIC_DATASET_ICU}.icustays` icus
),
-- Get the demographic for each patient, set to male as higher likelihood of readmission
demographics AS (
    SELECT
        subject_id,
        anchor_age as age,
        CASE WHEN gender = 'M' THEN 1 ELSE 0 END as is_male
    FROM `{MIMIC_PROJECT}.{MIMIC_DATASET_HOSP}.patients`
),
-- Get the diagnosis counts for each patient
diagnosis_counts AS (
    SELECT
        hadm_id,
        COUNT(DISTINCT icd_code) as num_diagnoses
    FROM `{MIMIC_PROJECT}.{MIMIC_DATASET_HOSP}.diagnoses_icd`
    GROUP BY hadm_id
),
-- Get the procedure counts for each patient for repeat admission
procedure_counts AS (
    SELECT
        hadm_id,
        COUNT(*) as num_procedures
    FROM `{MIMIC_PROJECT}.{MIMIC_DATASET_HOSP}.procedures_icd`
    GROUP BY hadm_id
),
-- Get the number of prior ICU stays for each patient for repeat admission
prior_icu AS (
    SELECT
        subject_id,
        stay_id,
        COUNT(*) OVER (PARTITION BY subject_id ORDER BY intime
                       ROWS BETWEEN UNBOUNDED PRECEDING AND 1 PRECEDING) as prior_icu_count
    FROM `{MIMIC_PROJECT}.{MIMIC_DATASET_ICU}.icustays`
),
-- Get the admission type, hospital LOS, and discharge location for each patient for severity of admission and length of stay and severity of discharge location
admission_info AS (
    SELECT
        hadm_id,
        CASE WHEN admission_type IN ('EMERGENCY', 'URGENT', 'AMBULATORY OBSERVATION',
                                     'DIRECT EMER.', 'EW EMER.', 'DIRECT OBSERVATION',
                                     'EU OBSERVATION', 'OBSERVATION ADMIT')
             THEN 1 ELSE 0 END as emergency_admission,
        DATETIME_DIFF(dischtime, admittime, DAY) as hospital_los_days,
        CASE WHEN discharge_location IN ('SKILLED NURSING FACILITY', 'REHAB', 'CHRONIC/LONG TERM ACUTE CARE', 'AGAINST ADVICE')
        THEN 1 ELSE 0 END as discharge_location_danger
    FROM `{MIMIC_PROJECT}.{MIMIC_DATASET_HOSP}.admissions`
)
-- Combine all the information into a single table
SELECT
    icus.*,
    dem.age,
    dem.is_male,
    -- COALESCE is used to handle missing values
    COALESCE(dx.num_diagnoses, 0) as num_diagnoses,
    COALESCE(proc.num_procedures, 0) as num_procedures,
    COALESCE(prior.prior_icu_count, 0) as prior_icu_count,
    COALESCE(adm.emergency_admission, 0) as emergency_admission,
    COALESCE(adm.hospital_los_days, 0) as hospital_los_days,
    COALESCE(adm.discharge_location_danger, 0) as discharge_location_danger,
    CASE
        WHEN DATETIME_DIFF(next_icu_intime, outtime, DAY) <= 30
        AND DATETIME_DIFF(next_icu_intime, outtime, DAY) >= 0
        THEN 1
        ELSE 0
    END as readmitted_30day
FROM icu_stays icus
-- Join all the information together
LEFT JOIN demographics dem ON icus.subject_id = dem.subject_id
LEFT JOIN diagnosis_counts dx ON icus.hadm_id = dx.hadm_id
LEFT JOIN procedure_counts proc ON icus.hadm_id = proc.hadm_id
LEFT JOIN prior_icu prior ON icus.stay_id = prior.stay_id
LEFT JOIN admission_info adm ON icus.hadm_id = adm.hadm_id
ORDER BY icus.subject_id, icus.intime
"""

print("Getting data from MIMIC-IV...")
df_readmissions = client.query(query).to_dataframe()

# Turn the readmissions data frame into the model data frame
df_model = df_readmissions.copy()
# converts care units into numerical values for interpretation
# remove all teh NaN from the model
df_model = df_model.dropna(subset=['icu_los_days'])
df_model = pd.get_dummies(df_model, columns=['first_careunit', 'last_careunit'], drop_first=True)
feature_cols = ['icu_los_days','age','is_male','num_diagnoses','num_procedures','prior_icu_count',] + [col for col in df_model.columns if 'careunit' in col]

#set model variables
X = df_model[feature_cols]
y = df_model['readmitted_30day']

print("Data Set Information"/n)
print("No Readmission: {(y==0).sum()}")
print("Readmission: {(y==1).sum()}")

# Training Criteria
print("Training Model...")
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=67,
    stratify=y
)

# Scale the values
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Run training
log_reg = LogisticRegression(
    random_state=67,
    max_iter=100,
    class_weight='balanced'
)

log_reg.fit(X_train_scaled, y_train)
print("Model Trained.")

# Make Predictions
y_prob = log_reg.predict_proba(X_test_scaled)[:, 1]
threshold = 0.502
y_pred = (y_prob >= threshold).astype(int)

# Build output to see how good the prediction model performed
print("-" * 54)
print("             Model Evaluation and Results")
print("-" * 54)
roc_auc = roc_auc_score(y_test, y_prob)
print( 'AUCROC Score: ',round(roc_auc, 3))
if roc_auc >= 0.8:
    print("Excellent Performance!")
elif roc_auc >= 0.7:
    print("Good Performance")
elif roc_auc >= 0.6:
    print("Decent Performance")
else:
    print("Needs Improvement")
print("-" * 54)
print("Classification Report")
print(classification_report(y_test, y_pred))
print("-" * 54)
print("Confusion Matrix")
print(confusion_matrix(y_test, y_pred))
print("-" * 54)
