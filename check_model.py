import pandas as pd

df = pd.read_csv("dataset/PhiUSIIL_Phishing_URL_Dataset.csv")

print("Dataset shape:", df.shape)

# Check whether any feature is identical or almost identical to the label
for column in df.columns:
    if column != "label":
        if df[column].nunique() <= 2:
            print(column, "unique values:", df[column].unique())

# Check duplicate URLs
print("\nDuplicate URLs:", df["URL"].duplicated().sum())

# Check duplicate complete rows
print("Duplicate rows:", df.duplicated().sum())

# Check relationship between some important features and label
print("\nLabel distribution:")
print(df["label"].value_counts())

print("\nHTTPS vs label:")
print(pd.crosstab(df["IsHTTPS"], df["label"]))