X = df[feature_cols]
y = df['readmitted_30day']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=67, stratify=y
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
    random_state=67
)

model.fit(X_train.values, y_train.to_numpy())

# Predictions
y_pred_prob = model.predict_proba(X_test.values)[:, 1]
y_pred = (y_pred_prob >= 0.2).astype(int)
