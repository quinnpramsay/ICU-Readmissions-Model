tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()

original_cost = 1855 * 15200
print("Original Cost of Readmissions: ","$","{:,}".format(original_cost))
missed_readmissions_cost = fn * 15200
print("Cost of People who were not readmitted: ","$","{:,}".format(missed_readmissions_cost))

wrongly_readmitted_cost = fp * 5000
print("Cost of People who were wrongly readmitted: ","$","{:,}".format(wrongly_readmitted_cost))

money_saved = tp * 15200 
print("Money saved from readmitions: ","$","{:,}".format(money_saved))

savings =missed_readmissions_cost + wrongly_readmitted_cost - money_saved

net_savings = original_cost - savings
print("Comparative savings from the model: " "$","{:,}".format(net_savings))
