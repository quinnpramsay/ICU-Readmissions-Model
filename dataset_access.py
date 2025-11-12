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


