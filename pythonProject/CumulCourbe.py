import pandas as pd
import matplotlib.pyplot as plt

# Load the data into a pandas DataFrame
df = pd.read_csv('febToJuin.csv',parse_dates=['date'])

df['date'] = pd.to_datetime(df['date'])


plt.figure(figsize=(100, 10))
plt.plot(df['date'], df['cumul'])
plt.xlabel('Date')
plt.ylabel('cumul')
plt.title('Variation de cumul')
plt.show()

