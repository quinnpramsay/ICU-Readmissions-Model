X = df[feature_cols]
y = df['readmitted_30day']

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=67,
    stratify=y
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

rf = RandomForestClassifier(
    n_estimators=500,                
    criterion='entropy',                
    max_depth=None,                  
    max_features='sqrt',                                            
    min_samples_split=5,             
    min_samples_leaf=2,              
    min_impurity_decrease=0.0,       
    class_weight='balanced',         
    bootstrap=True,
    max_samples=0.8,                 
    oob_score=True,                  
    n_jobs=-1,                       
    random_state=67,                    
    ccp_alpha=0.0  
)

print("Training Model...")
rf.fit(X_train_scaled, y_train)
print("Training complete")


y_prob = rf.predict_proba(X_test_scaled)[:, 1]
threshold = 0.2
y_pred = (y_prob >= threshold).astype(int)
