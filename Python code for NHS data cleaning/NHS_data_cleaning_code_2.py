"""This is my 2nd attempt at cleaning the NHS data ready for analysis.

I obtained this data set used in this program the following link:
https://digital.nhs.uk/data-and-information/publications/statistical/mental-health-services-monthly-statistics/final-may-provisional-june-2018

There is a publication for each month and as my initial method did not provide the correct results, I looked for
other files which could provide the data we need.

I noticed that the first row of the data in this file had the figure we need the figures we needed so I created a
function which would take in a list of files and then produce the cleaned versions ready to be joined together.

Below is the function i created:"""

# reading in pandas and the csv file

import pandas as pd

file_list = ['NHS_May_18', 'NHS_Jun_18', 'NHS_Jul_18', 'NHS_Aug_18', 'NHS_Sep_18', 'NHS_Oct_18', 'NHS_Nov_18',
             'NHS_Dec_18']


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


# iterating through the file list

for i in file_list:
    data = pd.read_csv(f"datasets/NHS_raw/{i}.csv")
    clean_nhs_data(data)
    CLEANED_DF.to_csv(f'datasets/NHS_cleaned/{i}_cleaned.csv', encoding='utf-8')

"""The plan was to join all these monthly files together in one file to form the full data set. Unfortunately, this 
function works for files between May 2018 and April 2019. After this, the file name stayed the same on each publication
but the content of the file changed and it no longer provided the figures we needed. Then the following year, the file
name was no longer published at all. Also, before May 2018, the day format was different so the function couldn't be
used on these files without having to amend the function slightly. However, even if these files has the same date 
format as the files i could use, we still wouldn't have had enough data to cover the time period we need due to the 
missing information."""
