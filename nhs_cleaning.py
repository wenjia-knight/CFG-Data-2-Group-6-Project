# reading in pandas and the csv file
import pandas as pd


def clean_nhs_data(data):
    global CLEANED_DF
    data_copy = data.copy()

    # drop irrelevant columns
    data_copy = data_copy[['REPORTING_PERIOD_START', 'MEASURE_ID', 'MEASURE_VALUE']]

    # rename columns
    data_copy.rename(columns={'REPORTING_PERIOD_START': 'month', 'MEASURE_ID': 'id',
                              'MEASURE_VALUE': 'new_referrals_sum'}, inplace=True)

    # convert datatypes to strings
    data_copy[['month', 'id', 'new_referrals_count']] = data_copy[['month', 'id', 'new_referrals_sum']].astype(
        "string")

    # remove * values
    data_copy = data_copy[~data_copy['new_referrals_sum'].isin(['*'])]

    # convert new_referrals_sum to float
    data_copy['new_referrals_sum'] = data_copy['new_referrals_sum'].astype("float")

    # convert month column to date
    data_copy['month'] = data_copy['month'].apply(pd.to_datetime, format='%d/%m/%Y')

    # filter by date range that we need
    date_filtered_df = data_copy.loc[(data_copy['month'] >= '2018-01-01')
                                     & (data_copy['month'] < '2023-01-01')]

    # sort into date order
    data_copy.sort_values(by=['month'], ascending=True, inplace=True)

    # filter by the reference for new referrals 'MHS32'
    id_date_filtered_df = date_filtered_df.loc[(data_copy['id'] == 'MHS32')]

    # sum up the values to get the total per month
    # having issues here because its not adding up again to what's on the power bi and i don't know why :(
    month_filtered_series = id_date_filtered_df.groupby('month')['new_referrals_sum'].sum()
    CLEANED_DF = pd.DataFrame(month_filtered_series)

    return CLEANED_DF


data = pd.read_csv("datasets/MHSDS Time_Series_data_Apr_2016_JanPrf_2023.csv")
clean_nhs_data(data)
CLEANED_DF.to_csv('datasets/NHS_data_cleaned.csv', encoding='utf-8')
