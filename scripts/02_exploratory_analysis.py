import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv("data/cleaned_sleep_data.csv")

# Summary statistics
print(df.describe())

# Plot distribution of Sleep Hours
plt.figure(figsize=(6,4))
sns.histplot(df["Sleep_Hours"], bins=10, kde=True)
plt.title("Distribution of Sleep Hours")
plt.xlabel("Hours")
plt.ylabel("Frequency")
plt.savefig("outputs/sleep_hours_distribution.png")
