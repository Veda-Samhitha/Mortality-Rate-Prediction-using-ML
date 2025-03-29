import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


df = pd.read_excel("Cleaned_COVID_Output.xlsx")

columns_to_drop = [col for col in ["location", "date"] if col in df.columns]
df_numeric = df.drop(columns=columns_to_drop)

if "life_expectancy" not in df_numeric.columns:
    raise KeyError("The column 'life_expectancy' is not found in the dataset.")

life_exp = df_numeric["life_expectancy"]
features_only = df_numeric.drop(columns=["life_expectancy"])

scaler = StandardScaler()
X_scaled = scaler.fit_transform(features_only)

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

plt.figure(figsize=(8, 6))
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=life_exp, cmap='viridis')
plt.colorbar(label="Life Expectancy")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("PCA: Life Expectancy Data")
plt.grid(True)
plt.tight_layout()
plt.show()

print("Explained Variance Ratio by each Principal Component:", pca.explained_variance_ratio_)
