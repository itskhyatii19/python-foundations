"""
Linear Regression from scratch using scikit-learn.

Steps:
1. Load and inspect data
2. Separate features and target
3. Train-test split
4. Train Linear Regression model
5. Evaluate using MAE, MSE, and R²
6. Visualising predictions vs actual data
"""

import pandas as pd

# Load a simple dataset
data = {
    "hours_studied": [1, 2, 3, 4, 5, 6, 7, 8],
"marks": [35, 40, 50, 60, 70, 75, 80, 85]
}

df = pd.DataFrame(data)

# Separate features and target
X = df[["hours_studied"]]
y = df["marks"]

print("Dataset:")
print(df)

print("\nFeatures (X):")
print(X)

print("\nTarget (y):")
print(y)

print("\nNumber of rows:", df.shape[0])
print("Number of features:", X.shape[1])

# Train-test split
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training samples:", X_train.shape)
print("Testing samples:", X_test.shape)


# Train Linear Regression model
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("Predictions:", predictions)
print("Actual values:", y_test.values)


# Evaluate using MAE, MSE, and R²
from sklearn.metrics import mean_absolute_error

mae = mean_absolute_error(y_test, predictions)
print("Mean Absolute Error:", mae)

from sklearn.metrics import mean_squared_error

mse = mean_squared_error(y_test, predictions)
print("Mean Squared Error:", mse)

from sklearn.metrics import r2_score

r2_score_value = r2_score(y_test, predictions)
print("R² Score:", r2_score_value)

# Visualize the results
import matplotlib.pyplot as plt
plt.scatter(X, y, color='blue', label='Data points')
plt.plot(X_test, predictions, color='red', linewidth=2, label='Regression line')
plt.xlabel('Hours Studied')     
plt.ylabel('Marks Obtained')
plt.title('Linear Regression: Hours Studied vs Marks Obtained')                                 
plt.legend()
plt.show()


