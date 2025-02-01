import pandas as pd
import numpy as np
import yfinance as yf
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Fetch stock data
data = yf.download('AAPL', start='2020-01-01', end='2023-01-01')
data['Prediction'] = data['Close'].shift(-30)

# Prepare data
X = data[['Close']].dropna()
y = data['Prediction'].dropna()

X_train, X_test, y_train, y_test = train_test_split(X[:-30], y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

# Predict next 30 days
future = np.array(data['Close'][-30:]).reshape(-1, 1)
predictions = model.predict(future)

print("Predicted Prices:", predictions)
