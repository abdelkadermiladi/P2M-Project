import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error

# Load the time series data into a Pandas DataFrame
df = pd.read_csv('anciens csv/df_february_2.csv')

# Convert the date column to a datetime type
df['date'] = pd.to_datetime(df['date'])

# Set the date column as the index of the DataFrame
df.set_index('date', inplace=True)

# Split the data into training and test sets
train = df[:int(0.7*(len(df)))]
test = df[int(0.7*(len(df))):]

# Fit the SARIMA model with order (2,1,4) on the training data
model = ARIMA(train['debit'], order=(2,1,4))
model = model.fit()

# Make predictions on the test data
predictions = model.predict(start=test.index[0], end=test.index[-1], dynamic=False)

# Calculate the mean squared error between the actual and predicted values
mse = mean_squared_error(test['debit'], predictions)
print("Mean Squared Error: ", mse)

print (predictions)