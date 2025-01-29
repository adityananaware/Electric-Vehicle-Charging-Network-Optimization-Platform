import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

# Load historical charging demand data
data = pd.read_csv('charging_demand.csv', parse_dates=['Date'], index_col='Date')

# Train ARIMA model
model = ARIMA(data['Demand'], order=(1,1,1))
model_fit = model.fit()

# Forecast demand for next 30 days
forecast = model_fit.forecast(steps=30)
print("Next 30-Day Demand Forecast:\n", forecast)
