import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv("data/sleep_deprivation_dataset_detailed.csv")

# Check for missing values
df = df.dropna()

# Encode categorical variables
encoder = LabelEncoder()
df["Gender"] = encoder.fit_transform(df["Gender"])

# Save cleaned dataset
df.to_csv("data/cleaned_sleep_data.csv", index=False)