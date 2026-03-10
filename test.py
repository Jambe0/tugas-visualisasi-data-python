import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data_kematian.csv")

plt.figure(figsize=(10,6))

for cause in df["Cause"].unique():
    subset = df[df["Cause"] == cause]
    plt.scatter(subset["Year"], subset["Total Deaths"], label=cause, alpha=0.6)

plt.xlabel("Year")
plt.ylabel("Total Deaths")
plt.title("Scatter Plot Total Deaths per Cause")
plt.legend()

plt.show()