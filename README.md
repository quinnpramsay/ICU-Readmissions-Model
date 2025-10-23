# Proposal
  Our idea is to create a machine learning model that predicts 30-day ICU readmission risk for patients over 18, using the dataset MIMIC from PhysioNet. We’ll use different types of information from these datasets, like labs, vitals, demographics, clinical notes, and X-ray scans. The goal is to show how tabular, text, and image data can be combined for a real-world healthcare problem that has both clinical and economic impact.

  We’ll mainly use the MIMIC-IV dataset, and we also want to look at different clinical trials and existing models to help improve our approach. On top of that, we’ll bring in Bio_ClinicalBERT from Kaggle for richer depictions and to help find hidden signals in data. 

  Since both of us are concetrate on Artificial Intelligence and Machine Learning, we think this project is a great way to practice and grow our skills. ICU readmissions are expensive and harmful for patients, so this project also shows how machine learning can improve predictions while touching on important ideas like clinical usefulness, data ethics, and explainability.

# Overview
 When it comes to patient health, ICU readmissions are associated with a six- to seven-fold increase in the odds of death, independent of other factors. This issue is evident not only nationally but also locally, particularly in the Piedmont region of North Carolina, where Surgical Trauma ICU readmissions are a notable concern. In this area, respiratory failure is the most common predictor of surgical trauma ICU readmission. Since our university is located within the Piedmont Triad, we hope that the research we conduct can help uncover the underlying factors driving this problem. In some studies, readmission rates can reach as high as 13.4% within just seven days, not even the full 30-day period that we are examining. Among patients receiving Medicare benefits, one in five is readmitted within 30 days, and 67% are readmitted within 90 days. These readmissions not only carry serious consequences for patient health but also impose a significant financial burden on hospitals. In 2004 alone, avoidable Medicare readmissions cost over $17 billion. Nationally, the total annual cost of patient readmissions exceeds $52.4 billion, with the average cost per readmission around $15,200. 

# Related Work Research
The problem with predicting risk of hospital readmissions was solved using several sources. These sources were classified in different categories. [1] being a data-driven model, [2] being in which the authors used clinical notes such as BERT, [3] talks about supervised learning and also risk models and finally [4] talks about the opposite of group [3] which is unsupervised learning and how it used techniques like clustering.

The group of structured data-driven models incorporates the paper about ICU readmission predictions using MIMIC-III structured EHR data.] A strength of this was how it demonstrated the functionality of standard classifiers on structured attributes. However, there is a weakness of how it is limited by the reliance on structured data and small sample sizes. Our project is wanting to expand past structured data by bringing text and imaging to help get a functioning model. 

Two papers are grouped with text and clinical notes with NLP. One paper talks about BERT and another uses C-path. In our project, we also plan on using Bio_ClinicalBERT for discharge notes. The strength of using this is to get richer depictions, and to help find hidden signals in data. Methods of text embedding require a lot of tuning. 

One of the papers talks about supervised learning and risk models. These learning examples show how machine learning can extend a physician's performance. These models however focus on tasks that physicians already do well at. In our project, we want to improve prediction in a complex problem where human accuracy is scarce. 

On the other hand, unsupervised learning was also talked about in the paper on heart failure readmission patients. It talked of methods of clustering, dimensionality reduction and phenotypic grouping and what they identified as subgroups with distinct risks and outcomes. This method does good at finding hidden patient subtypes, but it requires very large datasets. Our project will be mostly supervised learning, but maybe later on in the project we can incorporate multimodal embeddings to discover subgroups if needed. 

The current state-of-the-art methods in prediction ICU readmissions incorporate structured and unstructured data advanced techniques. Old methods like structured EHR data, Random Forest. Logistic regression and XGBoost are still very helpful and are powerful due to their interpretability. Recently individual work has incorporated unstructured clinical notes, using language models like BERT, and ClinicalBERT to help extract linguistic information that structured fields cannot grab. However, there are some barriers to worry about when using these state of the art methods. Some of these barriers can include the need for large datasets, computational cost and hyperameter tuning at scale.



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

- Genetic:
    This algorithm is an optimization technique that uses natural selection. This helps discover feature combinations that can’t be found through conventional techniques. This project will use it to optimize model hyperparameters and select the most relevant clinical features. 

Other Algorithms that have been used:
- XGBOOST:
    This is used most of the time on the dataset because of its speed, scalability and ability to handle data that is missing. This algorithm has a solid accuracy for mortality and readmission tasks.

- SVC:
    This method is helpful for dividing complex classes with small amounts of data. The only downside about this method is the expensiveness and it can be less interpretable. 

- Feed Foward:
    This is used in deep-learning studies on the MIMIC-III dataset for modeling complex dependencies. These models can be beneficial, but they lack transparency which can be less trustworthy. 

# Refrences

Inan, O. T., Tenaerts, P., Prindiville, S. A., Reynolds, H. R., Dizon, D. S., Cooper-Arnold, K., Turakhia, M. P., Pletcher, M. J., Preston, K. L., Krumholz, H. M., Marlin, B. M., Mandl, K. D., & Califf, R. M. (2020). Digitizing clinical trials. Journal of Personalized Medicine, 10(2), 21. https://doi.org/10.3390/jpm10020021 

Deo R. C. (2015). Machine learning in medicine. Circulation, 132(20), 1920–1930. doi:10.1161/CIRCULATIONAHA.115.001593 https://www.ahajournals.org/doi/full/10.1161/CIRCULATIONAHA.115.001593 

Toma, M., & Wei, O. C. (2023). Predictive modeling in medicine. Encyclopedia, 3(2), 590–601. doi:10.3390/encyclopedia3020042
https://www.mdpi.com/2673-8392/3/2/42 

Golas, S. B., Shibahara, T., Agboola, S., Otaki, H., Sato, J., Nakae, T., Hisamitsu, T., Kojima, G., Felsted, J., Kakarmath, S., Kvedar, J., & Jethwani, K. (2018). A machine learning model to predict the risk of 30-day readmissions in patients with heart failure: a retrospective analysis of electronic medical records data. BMC Medical Informatics and Decision Making, 18(1), 44.
https://link.springer.com/article/10.1186/s12911-018-0620-z 

Moerschbacher, A., & He, Z. (2023). Building prediction models for 30-day readmissions among icu patients using both structured and unstructured data in electronic health records. Proceedings. IEEE International Conference on Bioinformatics and Biomedicine, 2023, 4368–4373. 
https://doi.org/10.1109/bibm58861.2023.10385612 

Mcneill, H., & Khairat, S. (2020). Impact of intensive care unit readmissions on patient outcomes and the evaluation of the national early warning score to prevent readmissions: Literature review. JMIR Perioperative Medicine, 3(1), e13782. 
https://doi.org/10.2196/13782 

Beauvais, B., Whitaker, Z., Kim, F., & Anderson, B. (2022). Is the hospital value-based purchasing program associated with reduced hospital readmissions? Journal of Multidisciplinary Healthcare, 15, 1089–1099. 
https://doi.org/10.2147/JMDH.S358733 



