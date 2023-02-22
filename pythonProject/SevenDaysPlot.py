import pandas as pd
import matplotlib.pyplot as plt

# Chargez les données dans un DataFrame pandas
df = pd.read_csv('anciens csv/df2-5.csv', parse_dates=['date'])

start_date = pd.to_datetime('2022-05-23').date()
end_date = pd.to_datetime('2022-05-30').date()
week_data = df[(df['date'].dt.date >= start_date) & (df['date'].dt.date <= end_date)]

# Group les données par jour
day_groups = week_data.groupby(week_data['date'].dt.date)

# Trace les graphiques pour chaque jour
fig, axs = plt.subplots(len(day_groups), 1, figsize=(20, 20))
for i, (day, day_data) in enumerate(day_groups):
    axs[i].plot(day_data['date'], day_data['debit'])
    #axs[i].set_xlabel('Date')
    axs[i].set_ylabel('Débit')
    axs[i].set_title('Variation de débit pour le ' + day.strftime('%A %d %B %Y'))

# Adjust the spacing between the subplots
plt.subplots_adjust(hspace=1.5)

plt.show()
