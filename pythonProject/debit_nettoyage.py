import pandas as pd
#**********************************************************************
def find_max_consecutive_zeros(df):
    max_consecutive_zeros = 0
    current_consecutive_zeros = 0
    start_index = 0
    end_index = 0
    for index, row in df.iterrows():
        if row['debit'] == 0:
            current_consecutive_zeros += 1
        else:
            if current_consecutive_zeros > max_consecutive_zeros:
                max_consecutive_zeros = current_consecutive_zeros
                end_index = index - 1
                start_index = end_index - current_consecutive_zeros + 1
            current_consecutive_zeros = 0
    if current_consecutive_zeros > max_consecutive_zeros:
        max_consecutive_zeros = current_consecutive_zeros
        end_index = df.index[-1]
        start_index = end_index - current_consecutive_zeros + 1
    print("----------------------------------")
    print("Maximum consecutive zeros of debit: ", max_consecutive_zeros)
    print("----------------------------------")
    print("First row with maximum consecutive zeros:\n", df.loc[start_index])
    print("----------------------------------")
    print("Last row with maximum consecutive zeros:\n", df.loc[end_index])

#**********************************************************************
def extract_rows_and_find_maxconsecutive_zeros(df, start_date, end_date):
    extracted_rows = df[(df['date'] >= start_date) & (df['date'] <= end_date)]
    df_sortedEX = extracted_rows.sort_values(by='date')
    find_max_consecutive_zeros(df_sortedEX)

#**********************************************************************

# Load the data into a pandas DataFrame
df = pd.read_csv('FebMarAvr.csv')

df['date'] = pd.to_datetime(df['date'])

#debit
min_debit = df['debit'].min()
max_debit = df['debit'].max()

print("Min debit: ", min_debit)
print("Max debit: ", max_debit)

missing_values = df['debit'].isna().sum()
if missing_values > 0:
    print("There are missing values in the 'debit' column.")
else:
    print("There are no missing values in the 'debit' column.")


# Count the number of times the debit column has a value of 0
zero_debit_count = (df['debit'] == 0).sum()

print('Number of times debit = 0 est egal à ', zero_debit_count)

find_max_consecutive_zeros(df)

#########################################################

