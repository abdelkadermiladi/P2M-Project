import pandas as pd
# Load the data into a pandas DataFrame
df = pd.read_csv('FebMarAvr.csv')

cumul_diff = df['cumul'].diff()

if (cumul_diff >= 0).all():
    print("Cumuls are increasing")
else:
    print("Cumuls are not increasing !!!!!!!!!!!!!!!!")


df['cumul_diff'] = df['cumul'].diff()

# Find the rows where the difference is less than zero
rows_with_negative_cumul_diff = df[df['cumul_diff'] < 0]

# Display the rows with negative cumul difference
print(rows_with_negative_cumul_diff)


negative_cumul_diff = df[df['cumul_diff'] < 0]


missing_values = df['cumul'].isna().sum()
if missing_values > 0:
    print("There are missing values in the 'cumul' column.")
else:
    print("There are no missing values in the 'cumul' column.")

min = df['cumul_diff'].min()
print("minimun de la difference de cumul= ",min)

max = df['cumul_diff'].max()
print("maximum de la difference de cumul= ",max)

