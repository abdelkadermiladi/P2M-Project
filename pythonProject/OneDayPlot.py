import pandas as pd
import matplotlib.pyplot as plt

# Load the data into a pandas DataFrame
df = pd.read_csv('GlobalConsumptionSFM2_ETG2_Droppy_janv2022_janv2023.csv',parse_dates=['date'])

date_to_plot='2022-10-31'

fev_day = df[df['date'].dt.date == pd.to_datetime(date_to_plot).date()]


plt.figure(figsize=(100, 10))
plt.plot(fev_day['date'], fev_day['debit'])
plt.xlabel('Date')
plt.ylabel('debit')
plt.title('Variation de debit pour le '+ date_to_plot)
plt.show()

