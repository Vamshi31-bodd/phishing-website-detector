import pandas as pd
import joblib
import os
import sys

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

sys.path.append("src")

from feature_extraction import extract_features


# Load dataset
df = pd.read_csv("dataset/PhiUSIIL_Phishing_URL_Dataset.csv")

print("Dataset loaded:", len(df), "URLs")


# Extract URL-only features
print("Extracting URL features...")

feature_rows = []

for i, url in enumerate(df["URL"]):

    feature_rows.append(extract_features(url))

    if (i + 1) % 25000 == 0:
        print("Processed:", i + 1)


X = pd.DataFrame(feature_rows)
y = df["label"]


print("\nFeatures extracted successfully!")
print("Feature shape:", X.shape)


# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# Train model
print("\nTraining model...")

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)


# Evaluate
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("\nModel trained successfully!")
print("Accuracy:", accuracy)

print("\nClassification Report:")
print(classification_report(y_test, predictions))


# Save model
os.makedirs("models", exist_ok=True)

joblib.dump(
    {
        "model": model,
        "features": list(X.columns)
    },
    "models/phishing_model.pkl"
)

print("\nModel saved successfully!")
print("Location: models/phishing_model.pkl")