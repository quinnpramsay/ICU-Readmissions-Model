
# Overview
 When it comes to patient health, ICU readmissions are associated with a six to seven fold increase in the odds of death, independent of other factors. This issue is evident not only nationally but also locally, particularly in the Piedmont region of North Carolina, where Surgical Trauma ICU readmissions are a notable concern. In this area, respiratory failure is the most common predictor of surgical trauma ICU readmission. Since our university is located within the Piedmont Triad, we hope that the research we conduct can help uncover the underlying factors driving this problem. In some studies, readmission rates can reach as high as 13.4% within just seven days, not even the full 30-day period that we are examining. Among patients receiving Medicare benefits, one in five is readmitted within 30 days, and 67% are readmitted within 90 days. These readmissions not only carry serious consequences for patient health but also impose a significant financial burden on hospitals. In 2004 alone, avoidable Medicare readmissions cost over $17 billion. Nationally, the total annual cost of patient readmissions exceeds $52.4 billion, with the average cost per readmission around $15,200. 



# The Dataset
  For our project, we chose to use the MIMIC-IV dataset, version 3.1, available through PhysioNet. We gained access to this dataset by completing the "Data or Specimens Only Research" certification, which allows researchers to work with medical data. The Medical Information Mart for Intensive Care (MIMIC)-IV is a large, de-identified dataset containing information on patients admitted to the emergency department (ED) or an intensive care unit (ICU) at the Beth Israel Deaconess Medical Center in Boston, MA. MIMIC-IV includes hospital and critical care data for patients admitted between 2008 and 2022, covering over 65,000 ICU admissions and more than 200,000 ED visits.

MIMIC-IV is organized into two main components: ICU and HOSP. The HOSP module contains hospital wide data extracted from electronic health records, including demographics, admissions, and laboratory results. The ICU module, on the other hand, provides detailed clinical information such as vital signs, medications, and fluid inputs. This rich dataset is particularly valuable for our project, as it allows us to develop predictive models using multiple types of algorithms tailored to different data types.

Because the dataset is large, around 10 GB, we accessed it through Google BigQuery. Inside Google BigQuery you create your own project, and then use SQL to create your own dataset from the datasets you have access to. If you would like to see the query we used to make our dataset before the modifications within our models, check out the "gbq_dataset_create.sql" file and then the "dataset_access.py". The "gbq_dataset_create.sql" file shows teh query we made inside Google BigQuery (GBQ) to create a dataset of meaningful numerical values from the MIMIC-IV 3.1 datset, and the "dataset_access.py" file shows how we access GBQ from Google Colab or Jupyter Notebook and create mapping edits so all values in our dataset are integers. 

# Logistic Regression
Logistic Regression is a method used to predict probability of a binary outcome i.e. yes/no 1/0. This works by using the logistic function to model the relation between variables in the dataset and transforming the output as a probability between 1 and 0. For the logistic regression model you chose a threshold that is the decision marker, for ours it being .52.
Logistic Regression models look like a sigmoid function between 0 and 1 based on a given output that is a yes or no, like if someone was readmitted into the ICU. 

To run the Logistic Regression model, given in the files under "icu_logistic_regression.py" you will need to make sure that the dataset fits the same as the "gbq_dataset_create.sql" query. Then you have to set any non numerical values from the dataset to numerical values and then use the scaler function from sklearn to overall fit each type of value into the model at the same size. The output from our model looks like this. 

# Random Forest 
Random Forest is a machine learning method used for classification and regression. It generates multiple decision trees during training and combines their outputs to improve prediction accuracy and reduce overfitting. Each tree is trained on a random subset of the data and considers a random subset of features when making splits. For classification tasks, the final prediction is determined by a majority vote across all trees, while for regression tasks, predictions are averaged. Random Forest models are particularly effective at capturing complex relationships in the data and can handle large datasets with diverse variables. In the context of ICU readmission, the model estimates the likelihood of a patient being readmitted, which can then be compared to a threshold to make a yes/no prediction.

To run the Random Forest model you will see two different random forest codes in our github. "icu_random_forest.py" file is our own built code for random forest without using an inhereted library. "random_forest_Q.py" is our version with the inhereted function. To run the code just do the same thing as Logistic Regression model adding all the compnents together from all the files and ensuring your dataset is the same complete one we have, and then running it. 

# XGBoost
XGBoost (Extreme Gradient Boosting) is an advanced machine learning algorithm that constructs a sequence of decision trees, with each new tree designed to correct the errors of the previous ones. The algorithm optimizes a loss function using gradient descent and incorporates regularization techniques to prevent overfitting. XGBoost is highly efficient and performs well on large datasets with numerous features. For ICU readmission prediction, the algorithm produces a probability score for each patient, representing the risk of readmission. This score can be compared to a selected threshold to classify patients as likely or unlikely to be readmitted. XGBoost often achieves higher predictive accuracy than single-tree models because it iteratively focuses on the cases that are most difficult to predict.

Implementation of XGBoost is simular to the last two. Access the "icu_xgboosy.py" code and make sure to implement all the needed previous codes and the dataset from Google BigQuery. If everything is correct for the pieces beforehand, then all the Machine Learning Models should be interchangable. 

# Results

When evaluating the performance of predictive models, there are several approaches commonly used in other studies. One approach focuses on patient outcomes, prioritizing the highest recall rate to minimize the number of patients readmitted by ensuring that at-risk patients are correctly identified. Another approach emphasizes the statistical performance of the model, optimizing metrics such as precision, accuracy, and the area under the receiver operating characteristic curve (AUC-ROC) to assess the overall quality and reliability of predictions. While both approaches can be valid, this project adopted a different methodology due to the inherent limitations of relying solely on these metrics.
In this project, model quality was assessed not only based on AUC-ROC, accuracy, and precision but also on the financial impact of the predictions. To calculate this, the confusion matrix was used, detailing the model’s predictions as true positives, true negatives, false positives, and false negatives. Financial data obtained from previous research and studies were applied to determine the costs associated with patients not readmitted, the costs of false readmissions, and the savings achieved by preventing unnecessary readmissions. This information was then used to calculate the net financial savings relative to a scenario in which the model had not been implemented.
The following table summarizes the performance metrics and financial impact for each predictive model:

Logistic Regression
- AUC-ROC Score: 0.74
- Accuracy: 76%
- Precision: 59.5%
- Recall: 57%
- Original Cost: $28,196,000
- Comparative Savings: $16,315,200

Random Forest
- AUC-ROC Score: 0.744
- Accuracy: 76%
- Precision: 59%
- Recall: 56%
- Original Cost: $28,196,000
- Comparative Savings: $16,162,200


XGBoost
- AUC-ROC Score: 0.758
- Accuracy: 83%
- Precision: 62.5%
- Recall: 45%
- Original Cost: $28,196,000
- Comparative Savings: $16,811,000

# Conclusion 

 This project assessed the performance of three predictive models, Logistic Regression, Random Forest, and XGBoost, using both statistical metrics and financial impact to evaluate model quality. XGBoost achieved the highest AUC-ROC score of 0.758 and accuracy of 83 percent, though its recall rate was lower at 45 percent compared to Logistic Regression at 57 percent and Random Forest at 56 percent. Logistic Regression demonstrated a balanced performance with strong recall and substantial financial savings of $16,315,200. Random Forest showed similar predictive performance but slightly lower savings of $16,162,200. XGBoost, while lower in recall, generated the highest comparative financial savings at $16,811,000. These results highlight the trade-offs between accuracy, recall, and financial impact in predictive modeling for ICU readmissions.

 Overall, all three models demonstrated significant potential to reduce the costs associated with unnecessary readmissions, with comparative savings exceeding $16 million in each case. The findings emphasize that evaluating predictive models in healthcare requires considering both clinical outcomes and economic impact. Logistic Regression provided the most balanced approach between identifying at-risk patients and maximizing recall, while XGBoost excelled in overall predictive accuracy and achieved the highest financial savings. These insights underscore the importance of selecting models that align with both patient care objectives and operational priorities in healthcare settings.


# Resources

[1] Alsentzer, E. (2020). Bio_ClinicalBERT [Pretrained language model]. HuggingFace. https://huggingface.co/emilyalsentzer/Bio_ClinicalBERT

[2] Beauvais, B., Whitaker, Z., Kim, F., & Anderson, B. (2022). Is the hospital value-based purchasing program associated with reduced hospital readmissions? Journal of Multidisciplinary Healthcare, 15, 1089–1099. https://doi.org/10.2147/JMDH.S358733

[3] Blinder, Y. (n.d.). all_data.sql [SQL script]. GitHub. https://github.com/YaronBlinder/MIMIC-III_readmission/blob/master/all_data.sql

[4] Deo, R. C. (2015). Machine learning in medicine. Circulation, 132(20), 1920–1930. https://doi.org/10.1161/CIRCULATIONAHA.115.001593

[5] Golas, S. B., Shibahara, T., Agboola, S., Otaki, H., Sato, J., Nakae, T., Hisamitsu, T., Kojima, G., Felsted, J., Kakarmath, S., Kvedar, J., & Jethwani, K. (2018). A machine learning model to predict the risk of 30-day readmissions in patients with heart failure: A retrospective analysis of electronic medical records data. BMC Medical Informatics and Decision Making, 18(1), 44. https://doi.org/10.1186/s12911-018-0620-z

[6] Inan, O. T., Tenaerts, P., Prindiville, S. A., Reynolds, H. R., Dizon, D. S., Cooper-Arnold, K., Turakhia, M. P., Pletcher, M. J., Preston, K. L., Krumholz, H. M., Marlin, B. M., Mandl, K. D., & Califf, R. M. (2020). Digitizing clinical trials. Journal of Personalized Medicine, 10(2), 21. https://doi.org/10.3390/jpm10020021

[7] McNeill, H., & Khairat, S. (2020). Impact of intensive care unit readmissions on patient outcomes and the evaluation of the national early warning score to prevent readmissions: Literature review. JMIR Perioperative Medicine, 3(1), e13782. https://doi.org/10.2196/13782

[8] Moerschbacher, A., & He, Z. (2023). Building prediction models for 30-day readmissions among ICU patients using both structured and unstructured data in electronic health records. In Proceedings of the IEEE International Conference on Bioinformatics and Biomedicine (pp. 4368–4373). https://doi.org/10.1109/bibm58861.2023.10385612

[9] PhysioNet. (2023). MIMIC-IV (version 3.1). https://physionet.org/content/mimiciv/3.1

[10] Toma, M., & Wei, O. C. (2023). Predictive modeling in medicine. Encyclopedia, 3(2), 590–601. https://doi.org/10.3390/encyclopedia3020042




