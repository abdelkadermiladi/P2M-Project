import pandas as pd
mois_number=11
# Load the data into a pandas DataFrame
df = pd.read_csv("df2-"+str(mois_number)+".csv", parse_dates=['date'])

days_off = ["2022-03-20", "2022-04-09", "2022-05-01", "2022-05-04", "2022-07-25", "2022-07-10", "2022-07-30", "2022-08-13", "2022-10-15", "2022-10-08", "2022-12-17"]

# Parcourir la liste des jours de congé et mettre à zéro les valeurs de "debit" correspondantes
for day in days_off:
    df.loc[df['date'].dt.date == pd.to_datetime(day).date(), 'debit'] = 0

# Save the updated data to a new csv file
df.to_csv("df2-"+str(mois_number)+".csv", index=False)
