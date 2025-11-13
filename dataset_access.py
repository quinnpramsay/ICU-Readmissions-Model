# Access data using Google BigQuery.
from google.colab import auth
from google.cloud import bigquery

# Run for authorization
auth.authenticate_user()

# Input your project id for access
project_id='icu-readmissions-ai-project'
client = bigquery.Client(project=project_id)

# MIMIC-IV v3.1 dataset information making query easier if done through Jupyter Notebook
MIMIC_PROJECT = "physionet-data"
MIMIC_DATASET_HOSP = "mimiciv_3_1_hosp"
MIMIC_DATASET_ICU = "mimiciv_3_1_icu"

query = """
SELECT *
FROM `model_data.icu_survivors`
"""

df_readmissions = client.query(query).to_dataframe()

df = df_readmissions.copy()

df['gender'] = df['gender'].map({'M': 1, 'F': 0})

admission_type_mapping = {
    'SURGICAL SAME DAY ADMISSION': 0,
    'EU OBSERVATION': 1,
    'OBSERVATION ADMIT': 1,
    'URGENT': 2,
    'EW EMER.': 3 ,

}

df['admission_type'] = df['admission_type'].map(admission_type_mapping)

admission_location_mapping = {
    'WALK-IN/SELF REFERRAL': 0,
    'AMBULATORY SURGERY TRANSFER': 1,
    'PHYSICIAN REFERRAL': 1,
    'CLINIC REFERRAL': 1,
    'PROCEDURE SITE': 2,
    'PACU': 2,
    'INTERNAL TRANSFER TO OR FROM': 2,
    'TRANSFER FROM SKILLED NURSING': 3,
    'TRANSFER FROM HOSPITAL': 3,
    'EMERGENCY ROOM': 4,
    'INFORMATION NOT AVAILABLE': 0,

}

df = df[df['discharge_location'] != 'DIED']

df['admission_location'] = df['admission_location'].map(admission_location_mapping)

discharge_location_mapping = {
    'HOME': 0,
    'HOME HEALTH CARE': 1,
    'AGAINST ADVICE': 2,
    'ASSISTED LIVING': 2,
    'OTHER FACILITY': 2,
    'HEALTHCARE FACILITY': 3,
    'PSYCH FACILITY': 3,
    'ACUTE HOSPITAL': 3,
    'CHRONIC/LONG TERM ACUTE CARE': 4,
    'HOSPICE': 4,

}

df['discharge_location'] = df['discharge_location'].map(discharge_location_mapping)

df['discharge_location'] = df['discharge_location'].fillna(0)
df['admission_type'] = df['admission_type'].fillna(0)
df['admission_location'] = df['admission_location'].fillna(0)
df['drg_severity'] = df['drg_severity'].fillna(0)
df['length_of_stay'] = df['length_of_stay'].fillna(0)
df[ 'drg_mortality'] = df[ 'drg_mortality'].fillna(0)

feature_cols = [
    'length_of_stay',
    'age',
    'gender',
    'drg_severity',
    'admission_type',
    'admission_location',
    'discharge_location',
    'hospital_days',
    'prior_icu_admits_last_year',
    'num_procedures',
    'num_diagnoses',
    'drg_mortality',
    'days_since_last_icu',
    'chf',
    'cad',
    'diabetes',
    'copd',
    'ckd',
    'afib',
    'cancer',
    'los_category',
     'num_specimens',         
          'total_lab_events',         
        'num_icd_procedures',          
           'num_micro_tests',          
             'num_lab_items',          
            'num_diagnoses',          
         'max_diagnosis_seq',           
      'num_unique_icd_codes',         
'num_unique_procedure_codes',         
    'num_unique_micro_tests',          
  'num_organisms_identified',         
        'num_pharmacy_items',          
 'total_med_administrations',          
             'has_infection',

]
