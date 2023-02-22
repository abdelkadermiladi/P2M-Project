import pandas as pd
# Load both files into separate DataFrames
df2 = pd.read_csv("df2-10_30.csv")
df3 = pd.read_csv("df2-10_31.csv")


# Find the index of the row where you want to insert the new data
#insert_index = march_rows[march_rows['date'] == '2022-03-05 05:13:54'].index[0]

# Concatenate the two DataFrames together
#result = pd.concat([march_rows.iloc[:insert_index], hi_data, march_rows.iloc[insert_index:]])
result = pd.concat([df2, df3])
# Write the result to a new CSV file
result.to_csv("df2-10_new.csv", index=False)
