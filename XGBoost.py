from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, roc_auc_score

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
    )

model = XGBClassifier(
    n_estimators=200,       # number of trees
    learning_rate=0.05,     # shrinkage
    max_depth=4,            # tree depth
    subsample=0.8,          # row subsampling
    colsample_bytree=0.8,   # feature subsampling
    reg_lambda=1.0,         # L2 regularization
    objective='binary:logistic',
    eval_metric='logloss',  # or 'auc'
    n_jobs=-1,              # use all cores
    random_state=42
)

model.fit(X_train, y_train)

# Predictions
y_pred_prob = model.predict_proba(X_test)[:, 1]
y_pred = (y_pred_prob >= 0.5).astype(int)

acc = accuracy_score(y_test, y_pred)
auc = roc_auc_score(y_test, y_pred_prob)

print("Accuracy:", acc)
print("ROC AUC:", auc)
