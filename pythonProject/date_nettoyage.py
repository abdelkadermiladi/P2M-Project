import pandas as pd
import numpy as np
# Load the data into a pandas DataFrame
df = pd.read_csv('df2-11.csv')

# Convert the "date" column to datetime format
df['date'] = pd.to_datetime(df['date'])

missing_values = df['date'].isna().sum()
if missing_values > 0:
    print("There are missing values in the 'date' column.")
else:
    print("There are no missing values in the 'date' column.")


# check if there are any duplicate rows based on the "date" column
duplicates = df[df.duplicated(subset='date')]

# print the number of duplicates found
print("Number of duplicates found:", len(duplicates))

# if there are any duplicates, print them
if len(duplicates) > 0:
    print("Duplicate dates:")
    print(duplicates)



# Calculate the time difference between each row
df['time_difference'] = df['date'].diff().dt.total_seconds()

k=0
# Loop through each row and check if the time difference is equal to 15 seconds
for i in range(1, len(df)):
    if (10.0 > df.loc[i, 'time_difference']) or (df.loc[i, 'time_difference']>30.0):
        k = k+1
print("Nombre de fois le saut de lignes n'est pas dans l'intervalle [10 30] est: ", k)


min_time_diff = df['time_difference'].min()
max_time_diff = df['time_difference'].max()
print("Minimum time difference: ", min_time_diff)
print("Maximum time difference: ", max_time_diff)

# Sort the 'time_difference' column in descending order
df = df.sort_values('time_difference', ascending=False)
# Reset the index of the dataframe
df = df.reset_index(drop=True)

for i in range(1,13):
    print(f"{i}th Maximum time difference=", df.iloc[i-1]['time_difference'])

max_time_diff = df['time_difference'].max()
max_time_diff_row = df[df['time_difference'] == max_time_diff]
print("The rows with the maximum time difference:")
print(max_time_diff_row)


min_time_diff_row = df['time_difference'].idxmin()
print("row of the minimun time difference=", min_time_diff_row)


print('********************************************************************************')

df['hour'] = df['date'].dt.hour
mask = (df['hour'] >= 10) & (df['hour'] <= 11)
df_filtered = df.loc[mask]
df_sorted = df_filtered.sort_values(by='date')
print(df_sorted)

print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

def extract_rows_and_calculate_max_time_difference(df, start_date, end_date):
    start_date = pd.Timestamp(start_date)
    end_date = pd.Timestamp(end_date)

    extracted_rows = df[(df['date'] >= start_date) & (df['date'] <= end_date)]
    df_sortedEX = extracted_rows.sort_values(by='date')

    df_sortedEX['time_difference'] = df_sortedEX['date'].diff().dt.total_seconds()
    max_time_diffEX = df_sortedEX['time_difference'].max()
    print("For the extracted data between",start_date,"and ",end_date ," the maximum time difference : ", max_time_diffEX, "et number of rows: ", len(df_sortedEX))

print('\n')

