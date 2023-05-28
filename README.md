![image](https://github.com/wenjia-knight/CFG-Data-2-Group-6-Project/blob/main/Jupyter%20Notebooks/images/grouplogocolour.png "group logo")

# CFG-Data-2-Group-6-Project
This repo contains datasets, Python scripts and Jupyter Notebooks used for Group 6 Project as part of the CFGDegree (Data stream) in Spring 2023.

## The aim of this project is to examine the relationship between the mood of music streamed in the UK in comparison to the UK COVID lockdown timeline and NHS mental health services referrals.


-----

## Table of contents
* [Information](#info)
* [Tools and Technologies Used](#tools-and-technologies-used)
* [Requirements](#requirements)
* [Files](#files)
* [Spotify API](#Spotifyapi)
* [How to Run](#howto)
* [Project status](#Project status)  
* [Authors and Acknowledgment](#Authors and Acknowledgment)  

## Information
For a detailed report on the questions we are trying to answer and our approach to this analysis please see the ***Group 6 Project Report.pdf***

## Tools and Technologies Used
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![Plotly](https://img.shields.io/badge/Plotly-%233F4F75.svg?style=for-the-badge&logo=plotly&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pycharm](https://img.shields.io/badge/PyCharm-000000.svg?&style=for-the-badge&logo=PyCharm&logoColor=white)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![Colab](https://img.shields.io/badge/Colab-F9AB00?style=for-the-badge&logo=googlecolab&color=525252)
![MySQL](https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white)
![Spotify](https://img.shields.io/badge/Spotify-1ED760?&style=for-the-badge&logo=spotify&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![Google Drive](https://img.shields.io/badge/Google%20Drive-4285F4?style=for-the-badge&logo=googledrive&logoColor=white)
![Markdown](https://img.shields.io/badge/Markdown-000000?style=for-the-badge&logo=markdown&logoColor=white)
![Slack](https://img.shields.io/badge/Slack-4A154B?style=for-the-badge&logo=slack&logoColor=white) 
![Zoom](https://img.shields.io/badge/Zoom-2D8CFF?style=for-the-badge&logo=zoom&logoColor=white)
![Notion](https://img.shields.io/badge/Notion-000000?style=for-the-badge&logo=notion&logoColor=white)

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
- tabulate

## Files

    ├── Project Report 
      └── Group 6 Project Report.pdf
      └── Group 6 Project Presentation.pdf

    ├── Jupyter Notebooks 
      └── 01_data_preprocessing_notebooks
        └── 01_Spotify data mood allocation.ipynb
        └── 02_ML_spotify.ipynb
      └── 02_data_cleaning_notebooks
        └── 01_charts_and_moods_cleaning.ipynb
        └── 02_cleaning_NHS_data_attempts_1&3.ipynb
        └── 03_NHS_manual_data_cleaning_notebook.ipynb
      └── 03_data_analysis_and_visualisation_notebooks 
        └── 01_popular_tracks_data_analysis_final_Vilma.ipynb
        └── 02_Mood_Data_Visualisations_Isobel.ipynb
        └── 03_EDA.ipynb
        └── 04_Statistical_Exploration_MH_data.ipynb
      └── Images

    ├── Python code for NHS data cleaning
      └── NHS_data_cleaning_code_2.py

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

## Project status

This project is now completed. However, to further build on the amazing work that has already been done,
here are some ideas to expand this project in future:

- Increase our data sizes, more data points would help establish findings more conclusively.
- Include more mood classes, four mood classes is not really enough detail to describe all music tracks.

## Authors and Acknowledgment
<a href="https://github.com/tum-wade" target="_blank">Autumn</a>   
<a href="https://github.com/amix1587" target="_blank">Ami</a>  
<a href="https://github.com/mordents" target="_blank">Isobel</a>    
<a href="https://github.com/ishaibrahim" target="_blank">Isha</a>    
<a href="https://github.com/vilma-s1" target="_blank">Vilma</a>  
<a href="https://github.com/wenjia-knight" target="_blank">Wenjia</a>   
 

