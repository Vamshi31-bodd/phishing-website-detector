# 🔐 Phishing Website Detector

A machine-learning based web application that analyzes website URLs and predicts whether they are potentially phishing or legitimate.

## Features

- URL-based phishing detection
- Machine Learning classification
- Random Forest algorithm
- URL feature extraction
- Prediction confidence
- Flask web interface
- Input URL validation

## Technologies Used

- Python
- Pandas
- Scikit-learn
- Random Forest
- Flask
- HTML
- CSS
- Joblib

## Project Structure

phishing_website_detector/

├── dataset/
├── models/
│   └── phishing_model.pkl
├── src/
│   ├── feature_extraction.py
│   └── predict.py
├── static/
│   └── style.css
├── templates/
│   └── index.html
├── app.py
├── train_model.py
├── explore_data.py
├── requirements.txt
└── README.md

## Dataset

The project uses the PhiUSIIL Phishing URL Dataset.

The model uses URL-based features extracted from the dataset.

## Machine Learning Model

Algorithm:

Random Forest Classifier

The current test accuracy is approximately:

99.47%

## How to Run

Install the required packages:

pip install -r requirements.txt

Start the application:

python app.py

Open the following address in your browser:

http://127.0.0.1:5000

Enter a URL and click "Check Website".

## Important Note

The prediction is based on machine-learning features extracted from the URL. A high confidence score does not guarantee that a website is safe or malicious. Users should verify suspicious websites using additional security tools and trusted sources.