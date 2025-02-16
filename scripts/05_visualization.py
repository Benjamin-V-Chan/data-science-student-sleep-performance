import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv("data/cleaned_sleep_data.csv")

# Scatter plot: Sleep Hours vs Reaction Time
plt.figure(figsize=(6,4))
sns.scatterplot(x=df["Sleep_Hours"], y=df["Stroop_Task_Reaction_Time"])
sns.regplot(x=df["Sleep_Hours"], y=df["Stroop_Task_Reaction_Time"], scatter=False)
plt.title("Sleep Hours vs Reaction Time")
plt.xlabel("Sleep Hours")
plt.ylabel("Reaction Time (ms)")
plt.savefig("outputs/sleep_vs_reaction.png")
