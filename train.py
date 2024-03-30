import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib


data    = pd.read_csv("data/price-prediction.csv")
X       = data[['PLOTS']]
y       = data['PRICE']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model   = LinearRegression()
model.fit(X_train, y_train)
train_score = model.score(X_train, y_train)
test_score = model.score(X_test, y_test)

print(f"Training R^2 Score: {train_score:.2f}")
print(f"Testing R^2 Score: {test_score:.2f}")

joblib.dump(model, 'linear_regression_model.pkl')
