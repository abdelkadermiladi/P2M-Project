import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

df=pd.read_csv('df2-11.csv', parse_dates=['date'])
mois_number=11

df['date'] = pd.to_datetime(df['date'])
df= df[~df.index.duplicated(keep='first')]
# Set the date column as the index
df.set_index('date', inplace=True)

# Filter the rows where the `month` attribute is equal to
df_month = df[df.index.month == mois_number]

df_first_30_days = df_month.loc[df_month.index <= df_month.index[0] + pd.DateOffset(days=29)]

df_month=df_first_30_days

# Create a list to store the datetime index
new_index = []

# Initialize the starting datetime as the first datetime in the index
current_datetime = df_month.index[0]

# Loop through the index and add the new datetime if the difference with the next one is more than 30 seconds
for i in range(0, len(df_month.index)):
    if (df_month.index[i] - current_datetime).total_seconds() > 30:
        while (df_month.index[i] - current_datetime).total_seconds() > 30:
            current_datetime = current_datetime + pd.Timedelta(seconds=15)
            new_index.append(current_datetime)
    new_index.append(df_month.index[i])
    current_datetime = df_month.index[i]


# Add the new datetime to the dataframe as the index and fill the missing values with NaN
df_month = df_month.reindex(new_index)
df_month.fillna(value={'debit': np.nan, 'cumul': np.nan}, inplace=True)

#df_february['time_of_day'] = df_february.index.hour * 3600 + df_february.index.minute * 60 + df_february.index.second
df_month['dayofweek'] = df_month.index.dayofweek
#df_february['hour'] = df_february.index.hour
df_month['Minute_of_day']=df_month.index.hour * 60 + df_month.index.minute


#randomly
# Identify the rows that have missing values in the "water rate" column
missing_rows = df_month[df_month['debit'].isna()]

# Iterate over the missing rows and fill in the missing values
for index, missing_row in missing_rows.iterrows():
    # Find the rows that have the same day of the week and minute of the day
    day_of_week = missing_row['dayofweek']
    minute_of_day = missing_row['Minute_of_day']
    same_time_rows = df_month[
        (df_month['dayofweek'] == day_of_week) & (df_month['Minute_of_day'] == minute_of_day)]


    # Randomly select a value from the "water rate" column of the rows that have the same day of the week and minute of the day
    #if same_time_rows['debit'].notnull().any():
    random_value = same_time_rows['debit'].dropna().sample().values[0]
    #else:
    # handle case where there are no non-null values in 'debit' column
        #random_value = 0  # or any other default value you choose.

    df_month.at[index, 'debit'] = random_value


df_saved=df_month.copy()
#remove the added columns
df_saved = df_saved.drop(columns=[ 'Minute_of_day','dayofweek'])

# reset the index and add the index values to a column named 'date'
df_saved.reset_index(inplace=True)
df_saved.rename(columns={'index': 'date'}, inplace=True)

df_saved.to_csv("df2-"+str(mois_number)+"_30.csv", index=False)