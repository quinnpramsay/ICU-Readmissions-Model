# Proposal
  Our idea is to create a machine learning model that predicts 30-day ICU readmission risk for patients over 18, using the dataset MIMIC from PhysioNet. We’ll use different types of information from these datasets, like labs, vitals, demographics, clinical notes, and X-ray scans. The goal is to show how tabular, text, and image data can be combined for a real-world healthcare problem that has both clinical and economic impact.

  We’ll mainly use the MIMIC-IV dataset, and we also want to look at different clinical trials and existing models to help improve our approach. On top of that, we’ll bring in Bio_ClinicalBERT from Kaggle for richer depictions and to help find hidden signals in data. 

  Since both of us are concetrate on Artificial Intelligence and Machine Learning, we think this project is a great way to practice and grow our skills. ICU readmissions are expensive and harmful for patients, so this project also shows how machine learning can improve predictions while touching on important ideas like clinical usefulness, data ethics, and explainability.

# Overview
  When it comes to patient health, ICU readmissions cause a 6 to 7 times higher odds of death independent of other factors. This issue is apparent nationally, but also locally specifically in the Piedmont region of North Carolina when it comes to Surgical Trauma ICU readmissions. The most common predictor for surgical trauma ICU readmissions within this area is respiratory failure. As our University is located within the Piedmont Triad our hope is that the research we conduct can help discover underlying factors causing this issue. In certain studies, readmission rates can get as high as 13.4 percent in just 7 days, not even the full 30 days that we are studying. When it comes to patients recieving Medicare benifits, one fifth of patients are readmitted within 30 days and 67% are readmitted within 90 days. Not only do these readmission rates have a patient health cost, they also have a national monetary costs for hospitals. the cost of just Medicare readmissions in 2004 was over 17 billion dollars of avoidable costs. Nationally the overall cost annually of patient readmission if over 52.4 billion dollars with the average cost being around $15,200. 

# Related Work Research
When researching 5 scholarly sources for the milestone, we found that with predicting ICU readmission and applying machine learning models, there are several methods that can take place. Below are the 5 papers that we put into groups.
- The group of structured data-driven models incorporates the paper about ICU readmission predictions using MIMIC-III structured EHR data. A strength of this was how it demonstrated the functionality of standard classifiers on structured attributes. However, there is a weakness of how it is limited by the reliance on structured data and small sample sizes. Our project is wanting to expand past structured data by bringing text and imaging to help get a functioning model. 
- Two papers are grouped with text and clinical notes with NLP. One paper talks about BERT and another uses C-path. In our project, we also plan on using Bio_ClinicalBERT for discharge notes. The strength of using this is to get richer depictions, and to help find hidden signals in data. Methods of text embedding require a lot of tuning. 
One of the papers talks about supervised learning and risk models. These learning examples show how machine learning can extend a physician's performance. These models however focus on tasks that physicians already do well at. In our project, we want to improve prediction in a complex problem where human accuracy is scarce. 
- On the other hand, unsupervised learning was also talked about in the paper on heart failure readmission patients. It talked of methods of clustering, dimensionality reduction and phenotypic grouping and what they identified as subgroups with distinct risks and outcomes. This was really good at finding hidden patient subtypes, but it required very large datasets. Our project will be mostly supervised learning, but maybe later on in the project we can incorporate multimodal embeddings to discover subgroups if needed. 
- The current state-of-the-art methods in prediction ICU readmissions incorporate structured and unstructured data advanced techniques. Old methods like structured EHR data, Random Forest. Logistic regression and XGBoost are still very helpful and are powerful due to their interpretability. Recently individual work has incorporated unstructured clinical notes, using language models like BERT, and ClinicalBERT to help extract linguistic information that structured fields cannot grab. However, there are some barriers to worry about when using these state of the art methods. Some of these barriers can include the need for large datasets, computational cost and hyperameter tuning at scale.


# The Dataset
  The dataset that we decided to use is the MIMIC-IV set 3.1 version from PhysioNet. How we got access to this dataset is through the "Data or Specimens Only Research" certifications to gain access to medical data. Medical Information Mart for Intensive Care (MIMIC)-IV, is a large deidentified dataset of patients admitted to the emergency department or an intensive care unit at the Beth Israel Deaconess Medical Center in Boston, MA. MIMIC-IV contains hospital and critical care data for patients admitted to the ED or ICU between 2008 - 2022. MIMIC-IV contains data for over 65,000 patients admitted to an ICU and over 200,000 patients admitted to the emergency department. MMIC-IV has two main components to it, ICU and HOSP. Hosp has hospital wide data from electronic health records that contain data, such as demographics, admissions, and laboratory results. While the icu module contains detailed clinical information from the intensive care unit, like vital signs, medications, and fluid inputs. This is all very useful data to use for our project as we can create a predictive model from this data using multipole differnt types of searching algorithms based on the data type. To get access to such a large dataset, as it is 10 GB, we had to gain access to the Google Big Query file to this dataset and query specific data through google collab.

Retrieved 94,458 ICU visits

Sample of data:
subject_id	gender	stay_id	hadm_id	outcome
10000032	F	39553978	29079034	0
10000690	F	37081114	25860671	0
10000980	F	39765666	26913865	0
10001217	F	37067082	24597018	0
10001217	F	34592300	27703517	0
10001725	F	31205490	25563031	0
10001843	M	39698942	26133978	1
10001884	F	37510196	26184834	1
10002013	F	39060235	23581541	0
10002114	M	34672098	27793700	0
10002155	F	33685454	23822395	0
10002155	F	31090461	28994087	0
10002155	F	32358465	20345487	1
10002348	F	32610785	22725460	0
10002428	F	33987268	28662225	0
10002428	F	38875437	28662225	0
10002428	F	34807493	20321825	0
10002428	F	35479615	23473524	0
10002430	M	38392119	26295318	0
10002443	M	35044219	21329021	0

Summary by Gender and Outcome:
gender	outcome	count
F	0	36501
F	1	5082
M	0	46607
M	1	6268


# Method

# Refrences
(Update at end with correct annotation)

https://pmc.ncbi.nlm.nih.gov/articles/PMC7709858/

https://pmc.ncbi.nlm.nih.gov/articles/PMC9113654/

https://pmc.ncbi.nlm.nih.gov/articles/PMC11271049/

https://physionet.org/content/mimiciv/3.1/#files-panel

https://huggingface.co/emilyalsentzer/Bio_ClinicalBERT


