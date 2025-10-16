# Proposal
  Our idea is to create a machine learning model that predicts 30-day ICU readmission risk for patients over 18, using public datasets like MIMIC and PhysioNet. We’ll use different types of information from these datasets, like labs, vitals, demographics, clinical notes, and X-ray scans. The goal is to show how tabular, text, and image data can be combined for a real-world healthcare problem that has both clinical and economic impact.

  We’ll mainly use the MIMIC-IV dataset along with other data from PhysioNet, and we also want to look at different clinical trials and existing models to help improve our approach. On top of that, we’ll bring in Bio_ClinicalBERT from Kaggle for richer depictions and to help find hidden signals in data. Even though we don’t have access to every kind of medical record, we think we can still build a strong model with the resources available.

  Since both of us are concetrate on Artificial Intelligence and Machine Learning, we think this project is a great way to practice and grow our skills. ICU readmissions are expensive and harmful for patients, so this project also shows how machine learning can improve predictions while touching on important ideas like clinical usefulness, data ethics, and explainability.

# Overview
  When it comes to patient health, ICU readmissions cause a 6 to 7 times higher odds of death independent of other factors. This issue is apparent nationally, but also locally specifically in the Piedmont region of North Carolina when it comes to Surgical Trauma ICU readmissions. The most common predictor for surgical trauma ICU readmissions within this area is respiratory failure. As our University is located within the Piedmont Triad our hope is that the research we conduct can help discover underlying factors causing this issue. In certain studies, readmission rates can get as high as 13.4 percent in just 7 days, not even the full 30 days that we are studying. When it comes to patients recieving Medicare benifits, one fifth of patients are readmitted within 30 days and 67% are readmitted within 90 days. Not only do these readmission rates have a patient health cost, they also have a national monetary costs for hospitals. the cost of just Medicare readmissions in 2004 was over 17 billion dollars of avoidable costs. Nationally the overall cost annually of patient readmission if over 52.4 billion dollars with the average cost being around $15,200. 

# The Dataset
  The dataset that we decided to use is the MIMIC-IV set from PhysioNet. The reason we chose this dataset over others is that this is one of the best publicly available sets, and is the most up to date version of the MIMIC set. We acquired this dataset from PhysioNet, which is a publicly available site that has countless medical clinical datasets that can be downlaoded and used for different models. MIMIC-IV contains hospital and critical care data for patients admitted to the ED or ICU between 2008 - 2019.

# Refrences
(Update at end with correct annotation)

https://pmc.ncbi.nlm.nih.gov/articles/PMC7709858/

https://pmc.ncbi.nlm.nih.gov/articles/PMC9113654/

https://pmc.ncbi.nlm.nih.gov/articles/PMC11271049/


