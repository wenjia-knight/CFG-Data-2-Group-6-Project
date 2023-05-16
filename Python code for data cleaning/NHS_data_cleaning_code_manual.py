import pandas as pd

# converting the file to a csv
data = pd.read_excel("datasets/NHS_manual_data.xlsx", sheet_name='Sheet1')
data.to_csv('datasets/NHS_manual_data_cleaned.csv', encoding='utf-8')



