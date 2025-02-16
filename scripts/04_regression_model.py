import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load cleaned dataset
df = pd.read_csv("data/cleaned_sleep_data.csv")

# Define features and target variable
X = df[["Sleep_Hours"]]
y = df["Stroop_Task_Reaction_Time"]

# Split dataset into train/test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate model
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse:.4f}")

# Save model performance
with open("outputs/regression_results.txt", "w") as f:
    f.write(f"Mean Squared Error: {mse:.4f}")
