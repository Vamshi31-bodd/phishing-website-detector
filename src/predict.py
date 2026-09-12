import joblib
import pandas as pd
from feature_extraction import extract_features


# Load trained model
saved_model = joblib.load("models/phishing_model.pkl")

model = saved_model["model"]
features = saved_model["features"]


def predict_url(url):

    # Extract URL features
    extracted = extract_features(url)

    # Put features in the same order as training
    data = {
        feature: extracted[feature]
        for feature in features
    }

    X = pd.DataFrame([data])

    # Prediction
    prediction = model.predict(X)[0]

    probabilities = model.predict_proba(X)[0]

    confidence = max(probabilities) * 100

    # PhiUSIIL labels:
    # 1 = Legitimate
    # 0 = Phishing
    if prediction == 1:
        result = "Legitimate Website"
    else:
        result = "Phishing Website"

    return result, confidence


if __name__ == "__main__":

    url = input("Enter a URL: ")

    result, confidence = predict_url(url)

    print("\nResult:", result)
    print("Confidence:", round(confidence, 2), "%")