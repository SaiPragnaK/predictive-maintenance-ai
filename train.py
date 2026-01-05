import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.utils import resample
import joblib
import os


os.makedirs("data", exist_ok=True)
os.makedirs("models", exist_ok=True)


try:
    df = pd.read_csv("data/ai4i2020.csv")
    print("✅ Dataset Loaded Successfully!")
except FileNotFoundError:
    print("❌ Error: 'data/ai4i2020.csv' not found.")
    print("Please download the 'ai4i2020.csv' file I provided and place it in a 'data' folder.")
    exit()


feature_columns = [
    'Type', 'Air temperature [K]', 'Process temperature [K]',
    'Rotational speed [rpm]', 'Torque [Nm]', 'Tool wear [min]'
]
X = df[feature_columns].copy()
y = df['Machine failure'] 

X['Type'] = X['Type'].map({'L': 0, 'M': 1, 'H': 2})


data_to_balance = pd.concat([X, y], axis=1)

df_majority = data_to_balance[data_to_balance['Machine failure'] == 0]
df_minority = data_to_balance[data_to_balance['Machine failure'] == 1]


df_minority_upsampled = resample(df_minority,
                                 replace=True,
                                 n_samples=len(df_majority), 
                                 random_state=42)


df_balanced = pd.concat([df_majority, df_minority_upsampled])


X_bal = df_balanced.drop('Machine failure', axis=1)
y_bal = df_balanced['Machine failure']

print(f"✅ Data balanced. New shape: {X_bal.shape}")


X_train, X_test, y_train, y_test = train_test_split(X_bal, y_bal, test_size=0.2, random_state=42, stratify=y_bal)


scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("⏳ Training Random Forest model...")
model = RandomForestClassifier(n_estimators=200, random_state=42, n_jobs=-1)
model.fit(X_train_scaled, y_train)


acc = model.score(X_test_scaled, y_test)
print(f"✅ Model trained successfully! Balanced Accuracy: {acc*100:.2f}%")


joblib.dump(model, "models/rf_model.joblib")
joblib.dump(scaler, "models/scaler.joblib")
joblib.dump(feature_columns, "models/feature_columns.joblib") 
print("💾 Model, Scaler, and Feature Columns saved successfully in 'models/' folder.")
