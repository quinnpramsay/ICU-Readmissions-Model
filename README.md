# Proposal
  Our idea is to create a machine learning model that predicts 30-day ICU readmission risk for patients over 18, using the dataset MIMIC from PhysioNet. We’ll use different types of information from these datasets, like labs, vitals, demographics, clinical notes, and X-ray scans. The goal is to show how tabular, text, and image data can be combined for a real-world healthcare problem that has both clinical and economic impact.

  We’ll mainly use the MIMIC-IV dataset, and we also want to look at different clinical trials and existing models to help improve our approach. On top of that, we’ll bring in Bio_ClinicalBERT from Kaggle for richer depictions and to help find hidden signals in data. 

  Since both of us are concetrate on Artificial Intelligence and Machine Learning, we think this project is a great way to practice and grow our skills. ICU readmissions are expensive and harmful for patients, so this project also shows how machine learning can improve predictions while touching on important ideas like clinical usefulness, data ethics, and explainability.

# Overview
 When it comes to patient health, ICU readmissions are associated with a six- to seven-fold increase in the odds of death, independent of other factors. This issue is evident not only nationally but also locally, particularly in the Piedmont region of North Carolina, where Surgical Trauma ICU readmissions are a notable concern. In this area, respiratory failure is the most common predictor of surgical trauma ICU readmission. Since our university is located within the Piedmont Triad, we hope that the research we conduct can help uncover the underlying factors driving this problem. In some studies, readmission rates can reach as high as 13.4% within just seven days, not even the full 30-day period that we are examining. Among patients receiving Medicare benefits, one in five is readmitted within 30 days, and 67% are readmitted within 90 days. These readmissions not only carry serious consequences for patient health but also impose a significant financial burden on hospitals. In 2004 alone, avoidable Medicare readmissions cost over $17 billion. Nationally, the total annual cost of patient readmissions exceeds $52.4 billion, with the average cost per readmission around $15,200. 



# The Dataset
  For our project, we chose to use the MIMIC-IV dataset, version 3.1, available through PhysioNet. We gained access to this dataset by completing the "Data or Specimens Only Research" certification, which allows researchers to work with medical data. The Medical Information Mart for Intensive Care (MIMIC)-IV is a large, de-identified dataset containing information on patients admitted to the emergency department (ED) or an intensive care unit (ICU) at the Beth Israel Deaconess Medical Center in Boston, MA. MIMIC-IV includes hospital and critical care data for patients admitted between 2008 and 2022, covering over 65,000 ICU admissions and more than 200,000 ED visits.

MIMIC-IV is organized into two main components: ICU and HOSP. The HOSP module contains hospital wide data extracted from electronic health records, including demographics, admissions, and laboratory results. The ICU module, on the other hand, provides detailed clinical information such as vital signs, medications, and fluid inputs. This rich dataset is particularly valuable for our project, as it allows us to develop predictive models using multiple types of algorithms tailored to different data types.

Because the dataset is large, around 10 GB, we accessed it through Google BigQuery and queried specific data using Google Colab, which enabled us to efficiently work with the information we needed for analysis.


# Method
Algorithms we will use:

- Logistic Regression:
    Logistic Regression is a method used to predict probability of a binary outcome i.e. yes/no 1/0. This works by using the logistic function to model the relation between variables in the dataset and transforming the output as a probability between 1 and 0. We will use a predefined value like 0.5 to move the outcome if it is over that to 1 or if not move it to 0.  

- Random Forest:
    This will be a bassline predictive model that will be used for establishing a reference for performance outcome. It takes it as a linear relationship between independent variables (like lab test values) and dependent variables (like readmission likelihood).

-XGBoost

#Resources
https://github.com/YaronBlinder/MIMIC-III_readmission/blob/master/all_data.sql
https://www.ahajournals.org/doi/full/10.1161/CIRCULATIONAHA.115.001593 
https://www.mdpi.com/2673-8392/3/2/42 
https://link.springer.com/article/10.1186/s12911-018-0620-z
https://doi.org/10.3390/jpm10020021 
https://pmc.ncbi.nlm.nih.gov/articles/PMC7709858/
https://doi.org/10.2147/JMDH.S358733 
https://pmc.ncbi.nlm.nih.gov/articles/PMC9113654/
https://pmc.ncbi.nlm.nih.gov/articles/PMC11271049/
https://physionet.org/content/mimiciv/3.1/#files-panel
https://huggingface.co/emilyalsentzer/Bio_ClinicalBERT



