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

df_readmissions = client.query(query).to_dataframe()

# Turn the readmissions data frame into the model data frame
df_model = df_readmissions.copy()
# converts care units into numerical values for interpretation
# remove all teh NaN from the model

feature_cols = 

#set model variables
X = df_model[feature_cols]
y = df_model['readmitted_30day']

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
threshold = 0.62
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
