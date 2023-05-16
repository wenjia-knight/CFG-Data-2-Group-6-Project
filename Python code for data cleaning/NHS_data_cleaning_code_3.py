# reading in pandas and the csv file
import pandas as pd


def clean_nhs_data(data):
    data_copy = data.copy()

    # drop irrelevant columns
    data_copy = data_copy[['REPORTING_PERIOD_START', 'MEASURE_ID', 'MEASURE_VALUE']]

    # rename columns
    data_copy.rename(columns={'REPORTING_PERIOD_START': 'month', 'MEASURE_ID': 'id',
                              'MEASURE_VALUE': 'new_referrals'}, inplace=True)

    # convert datatypes to strings
    data_copy[['month', 'id', 'new_referrals']] = data_copy[['month', 'id', 'new_referrals']].astype(
        "string")

    # remove * values
    data_copy = data_copy[~data_copy['new_referrals'].isin(['*'])]

    # convert new_referrals_sum to float
    data_copy['new_referrals'] = data_copy['new_referrals'].astype("float")

    # convert month column to date
    data_copy['month'] = data_copy['month'].apply(pd.to_datetime, format='%d/%m/%Y')

    # take just the first row
    global CLEANED_DF

    # filter by date range that we need
    date_filtered_df = data_copy.loc[(data_copy['month'] >= '2018-01-01')
                                     & (data_copy['month'] < '2023-01-01')]

    # sort into date order
    data_copy.sort_values(by=['month'], ascending=True, inplace=True)

    # filter by the reference for new referrals 'MHS32'
    id_date_filtered_df = date_filtered_df.loc[(data_copy['id'] == 'MHS32')]

    # sum up the values to get the total per month
    month_filtered_series = id_date_filtered_df.groupby('month')['new_referrals'].sum()
    CLEANED_DF = pd.DataFrame(month_filtered_series)

    return CLEANED_DF


data = pd.read_csv("datasets/NHS_raw/MHSDS Time_Series_data_Apr_2016_JanPrf_2023.csv")
clean_nhs_data(data)
CLEANED_DF.to_csv('datasets/NHS_cleaned/NHS_data_cleaned.csv', encoding='utf-8')
