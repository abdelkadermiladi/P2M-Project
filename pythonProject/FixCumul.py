import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

df_month=pd.read_csv('df2-7.csv', parse_dates=['date'])



for i in range(1, len(df_month)):
    df_month.at[i, 'cumul'] = df_month.at[i-1, 'cumul'] + df_month.at[i, 'debit']


df_month.to_csv("df2-7.csv", index=False)