X = df[feature_cols]
y = df['readmitted_30day']


print("Training Model...")
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=67,
    stratify=y
)

numeric_columns = X_train.select_dtypes(include=['int64', 'float64', 'int32', 'float32']).columns.tolist()

datetime_columns = X_train.select_dtypes(include=['datetime64', 'datetime64[ns]']).columns.tolist()
non_datetime_columns = [col for col in X_train.columns if col not in datetime_columns]


scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


log_reg = LogisticRegression(
    random_state=67,
    max_iter=100,
    class_weight='balanced'
)

log_reg.fit(X_train_scaled, y_train)


y_prob = log_reg.predict_proba(X_test_scaled)[:, 1]
threshold = 0.52
y_pred = (y_prob >= threshold).astype(int)
