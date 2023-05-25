![image](https://github.com/wenjia-knight/CFG-Data-2-Group-6-Project/blob/main/Jupyter%20Notebooks/images/grouplogocolour.png "group logo")

# CFG-Data-2-Group-6-Project
This repo contains datasets, Python scripts and Jupyter Notebooks used for Group 6 Project as part of the CFGDegree (Data stream) in Spring 2023.

## The aim of this project is to examine the relationship between the mood of music streamed in the UK in comparison to the UK COVID lockdown timeline and NHS mental health services referrals.


-----

## Table of contents
* [Information](#info)
* [Requirements](#requirements)
* [Files](#files)
* [Spotify API](#Spotifyapi)
* [How to Run](#howto)
* [Status](#status)
* [Creators](#creators)

## Information
For a detailed report on the questions we are trying to answer and our approach to this analysis please see the ***ProjectReport.pdf***

## Requirements
Please make sure you have installed the following Python packages before running the scripts and notebooks:
- Pandas
- NumPy
- Seaborn
- Matplotlib
- Scikit-learn
- Spotipy
- xlrd
- mysql-connector-python
- beautifulsoup4
- requests
- plotly
- joblib

## Files

    ├── Project Report 
      └── 1. ProjectReport.pdf 
      └── 2. ProjectLog.pdf
      └── 3. ProjectPresentation.pdf
      

    ├── Jupyter Notebooks 
      └── 01_data_preprocessing_notebooks
        └── 01_Spotify data mood allocation.ipynb
        └── 02_ML_spotify.ipynb
      └── 02_data_cleaning_notebooks
        └── 01_charts_and_moods_cleaning.ipynb
        └── 02_Cleaning NHS Data - Attempt 1 & 3.ipynb
        └── 03_Cleaning NHS Data - Attempt 2.ipynb
        └── 04_NHS_manual_data_cleaning_notebook.ipynb
      └── 03_data_analysis_and_visualisation_notebooks 
        └── 01_popular_tracks_data_analysis_final.ipynb
        └── 02_MultilinePlot_Isobel.ipynb
        └── 03_EDA.ipynb
      └── Images


    ├── Python code for NHS data cleaning
      └── nhs_cleaning2.py
      └── NHS_data_cleaning_code_1.py
      └── NHS_data_cleaning_code_2.py
      └── NHS_data_cleaning_code_3.py
      └── NHS_data_cleaning_code_manual.py

    ├── Python codes for web scraping & API
      └── 01_get_historical_charts.py
      └── 02_get_unique_isrc.py
      └── 03_get_spotify_ids.py
      └── 04_get_audio_features.py
      └── config.py

    ├── SQL database
      └── config.py
      └── create_database.py
      └── database_queries.ipynb
      └── EER diagram.png

    ├── Datasets
     
## Spotify API
To connect to the spotify API using your own client ID and client SECRET
you will need to create an account on <a href="https://developer.spotify.com/" target="_blank">Spotify Developer Sign-up</a>  
This page explains how to create your authorisation  <a href="https://developer.spotify.com/documentation/web-api/concepts/apps" target="_blank">Spotify Authorisation</a>

Then simply input your credentials when you see a CLIENT ID and CLIENT SECRET variable or in the config file if available. 

## mySQL database
To connect to mySQL database, please use your own root password and replace 'PASSWORD' in the config file in `SQL database` folder. 

## How to Run       

To get started, please clone the repository to your local machine. Run through the Jupyter Notebooks saved in `Jupyter Notebooks/03_data_analysis_and_visualisation_notebooks` to see the analysis and visualisation of the data shown in the report. 
All data used in this project is saved in the `Datasets` folder. 

Other folders in this repository are as follows (used to create the datasets):

- `Jupyter Notebooks/01_data_preprocessing_notebooks` contains the notebooks used to classify music moods using Machine Learning.
- `Jupyter Notebooks/02_data_cleaning_notebooks` contains the notebooks used to clean the NHS data and popular track moods data.
- `Python code for NHS data cleaning` contains the Python scripts used to clean the NHS data.
- `Python codes for web scraping & API` contains the Python scripts used to scrape the data from the Official Charts website and get audio features from the Spotify API.
- `SQL database` contains the Python script used to create the database and Juypter Notebook used to generate some example queries. Please note SQL database was not used in this project. It was 
created to show the process of creating a database and how to query the data.

## Status

IN PROGRESS

## Creators
<a href="https://github.com/wenjia-knight" target="_blank">Wenjia</a>  
<a href="https://github.com/tum-wade" target="_blank">Autumn</a>  
<a href="https://github.com/mordents" target="_blank">Isobel</a>  
<a href="https://github.com/vilma-s1" target="_blank">Vilma</a>  
<a href="https://github.com/ishaibrahim" target="_blank">Isha</a>  
<a href="https://github.com/amix1587" target="_blank">Ami</a>
