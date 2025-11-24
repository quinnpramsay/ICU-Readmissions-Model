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
