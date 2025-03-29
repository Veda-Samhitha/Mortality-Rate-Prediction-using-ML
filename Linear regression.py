import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import root_mean_squared_error, r2_score

df = pd.read_excel("Cleaned_COVID_Output.xlsx")

df = df.drop(columns=["location", "date"])

X = df.drop(columns=["life_expectancy"]) # This creates the input features (X) by removing the target column 'life_expectancy' from the dataset.
y = df["life_expectancy"]  # This sets the target variable (y), which is the column we want to predict.

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

lr_model = LinearRegression()
lr_model.fit(X_train, y_train)

y_pred = lr_model.predict(X_test)
rmse = root_mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Linear Regression Model Trained Successfully!")
print("RMSE:", round(rmse, 2))
print("R² Score:", round(r2, 2))

importance = pd.Series(lr_model.coef_, index=X.columns)
importance.sort_values().plot(kind='barh', figsize=(8,6), title="Linear Regression: Mortality Risk Features")
plt.xlabel("Coefficient Value")
plt.tight_layout()
plt.show()
