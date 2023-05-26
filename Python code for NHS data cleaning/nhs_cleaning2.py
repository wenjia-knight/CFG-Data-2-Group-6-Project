import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('NHS_manual_data_cleaned.csv', index_col=[0])
year = df.month.str[0:4]
df.insert(loc=0, column='year', value=year)
df['month'] = df.month.str[5:7]
df.drop(df.filter(regex="Unname"),axis=1, inplace=True)

df.to_csv('NHS_manual_data_cleaned_reformat.csv', encoding='utf-8', index=False)
df2 = pd.read_csv('NHS_manual_data_cleaned_reformat.csv')
df2.tail()