# reading in pandas and the csv file

import pandas as pd

file_list = ['NHS_May_18', 'NHS_Jun_18', 'NHS_Jul_18', 'NHS_Aug_18', 'NHS_Sep_18', 'NHS_Oct_18', 'NHS_Nov_18', 'NHS_Dec_18']


def clean_nhs_data(data):
    data_copy = data.copy()

    # drop irrelevant columns

    data_copy = data_copy[['REPORTING_PERIOD', 'MHS32 - Referrals starting in RP']]

    # rename columns
    data_copy.rename(columns={'REPORTING_PERIOD': 'month',
                              'MHS32 - Referrals starting in RP': 'new_referrals'}, inplace=True)

    # convert datatypes to strings

    data_copy[['month', 'new_referrals']] = data_copy[
        ['month', 'new_referrals']].astype("string")

    # convert date column to a datetime data type

    data_copy['month'] = data_copy['month'].apply(pd.to_datetime, format='%b-%y')

    data_copy['month'] = data_copy['month'].dt.strftime('%b%Y')

    # take just the first row

    global CLEANED_DF

    CLEANED_DF = data_copy.head(1)

    return CLEANED_DF


for i in file_list:
    data = pd.read_csv(f"datasets/NHS_raw/{i}.csv")
    clean_nhs_data(data)
    CLEANED_DF.to_csv(f'datasets/NHS_cleaned/{i}_cleaned.csv', encoding='utf-8')
