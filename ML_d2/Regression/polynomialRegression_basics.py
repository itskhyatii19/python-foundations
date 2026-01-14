import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

data = {
    "hours_studied": [1,2,3,4,5,6,7,8],
    "marks": [35,40,50,60,70,75,80,85]
}

df = pd.DataFrame(data)

X = df[["hours_studied"]]
y = df["marks"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

poly = PolynomialFeatures(degree=3, include_bias=True)

X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

model = LinearRegression()
model.fit(X_train_poly, y_train)

predictions = model.predict(X_test_poly)

mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("Polynomial Regression MAE:", mae)
print("Polynomial Regression R²:", r2)

X_full_poly = poly.transform(X)

plt.scatter(X, y, color="blue", label="Actual data")
plt.plot(X, model.predict(X_full_poly), color="red", label="Polynomial curve")

plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.title("Polynomial Regression (Degree 2)")
plt.legend()
plt.show()
