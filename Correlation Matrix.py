import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel("Cleaned_COVID_Output.xlsx")

columns_to_drop = [col for col in ["location", "date"] if col in df.columns]
df_numeric = df.drop(columns=columns_to_drop)

corr_matrix = df_numeric.corr()

plt.figure(figsize=(12, 10))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', cbar=True)
plt.title("Correlation Matrix of Features")
plt.tight_layout()
plt.show()
