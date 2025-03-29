import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np


df = pd.read_excel("Cleaned_COVID_Output.xlsx")

df = df.drop(columns=["location", "date"])

if "life_expectancy" not in df.columns:
    raise KeyError("The column 'life_expectancy' is not found in the dataset.")

X = df.drop(columns=["life_expectancy"])
y = df["life_expectancy"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print(" Random Forest Model Trained Successfully!")
print(" RMSE:", round(rmse, 2))
print(" R² Score:", round(r2, 2))
print(y_pred)

importances = model.feature_importances_
feature_names = X.columns

plt.figure(figsize=(10, 6))
plt.barh(feature_names, importances)
plt.xlabel("Relative Importance to Life Expectancy")
plt.title("Feature Importance - Random Forest")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()
