import mysql.connector
import datetime
from config import USER, PASSWORD, HOST

# Establish a connection to the local MySQL server:
mydb = mysql.connector.connect(
    host=HOST,
    user=USER,
    password=PASSWORD,
    auth_plugin='mysql_native_password',
)

# Create a new database using the CREATE DATABASE statement:
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE popular_tracks_and_features")

# Switch to the created database:
mycursor.execute("USE popular_tracks_and_features")

# Create the first table:
create_table1_query = """
CREATE TABLE isrc_table (
    isrc VARCHAR(255) NOT NULL PRIMARY KEY,
    title VARCHAR(255),
    artist VARCHAR(255)
)
"""
mycursor.execute(create_table1_query)

# Use the csv file to insert values to the table
with open('../datasets/unique_isrc.csv', 'r', newline='', encoding='utf-8') as file:
    csv_data = file.readlines()
    # skip the first header row
    for line in csv_data[1:]:
        values = line.strip().split(',')

        # Prepare the insert query with the correct format
        insert_query = "INSERT INTO isrc_table (isrc, title, artist) VALUES (%s, %s, %s)"

        # Pass the values to the execute method
        mycursor.execute(insert_query, values)

# Create the second table:
create_table2_query = """
CREATE TABLE tracks_in_charts (
    dates DATE,
    position INT,
    title VARCHAR(255),
    artist VARCHAR(255),
    label VARCHAR(255),
    isrc CHAR(12),
    FOREIGN KEY (isrc) REFERENCES isrc_table(isrc)
)
"""
mycursor.execute(create_table2_query)

# Use the csv file to insert values to the table
with open('../datasets/uk_top_singles_chart.csv', 'r', newline='', encoding='utf-8') as file:
    csv_data = file.readlines()
    for line in csv_data[1:]:
        values = line.strip().split(',')

        # Convert the 'dates' value to the correct format
        dates_value = datetime.datetime.strptime(values[0], '%d %B %Y').date()

        # Prepare the insert query with the correct format
        insert_query = "INSERT INTO tracks_in_charts (dates, position, title, artist, label, isrc) VALUES (%s, %s, %s, %s, %s, %s)"

        # Pass the converted date value to the execute method
        mycursor.execute(insert_query, (dates_value,) + tuple(values[1:]))

# Create a new table that contains all spotify IDs:
create_table3_query = """
CREATE TABLE spotify_table (
    isrc VARCHAR(255) NOT NULL PRIMARY KEY,
    artist VARCHAR(255),
    artist_spotify_id VARCHAR(255),
    track_name VARCHAR(255),
    track_spotify_id VARCHAR(255),
    FOREIGN KEY (isrc) REFERENCES isrc_table(isrc)
)
"""
mycursor.execute(create_table3_query)

# Use the csv file to insert values to the table
with open('../datasets/isrc_spotify_ids.csv', 'r', newline='', encoding='utf-8') as file:
    csv_data = file.readlines()
    for line in csv_data[1:]:
        values = line.strip().split(',')

        # Prepare the insert query with the correct format
        insert_query = "INSERT INTO spotify_table (isrc, artist, artist_spotify_id, track_name, track_spotify_id) VALUES (%s, %s, %s, %s, %s)"

        # Pass the values to the execute method
        mycursor.execute(insert_query, values)

# Create a new table that contains track features and moods:
create_table4_query = """
CREATE TABLE feature_table (
    isrc VARCHAR(255),
    track_name VARCHAR(255),
    track_spotify_id VARCHAR(255),
    acousticness FLOAT,
    danceability FLOAT,
    duration_ms INT,
    energy FLOAT,
    instrumentalness FLOAT,
    `key` INT,
    liveness FLOAT,
    loudness FLOAT,
    `mode` INT,
    speechiness FLOAT,
    tempo FLOAT,
    time_signature INT,
    valence FLOAT,
    mood VARCHAR(10),
    FOREIGN KEY (isrc) REFERENCES isrc_table(isrc)
)
"""
mycursor.execute(create_table4_query)

# Use the csv file to insert values to the table
with open('../datasets/track_audio_features_plus_mood_analysis.csv', 'r', newline='', encoding='utf-8') as file:
    csv_data = file.readlines()
    for line in csv_data[1:]:
        values = line.strip().split(',')[1:]

        # Prepare the insert query with the correct format
        insert_query = "INSERT INTO feature_table (isrc, track_name, track_spotify_id, acousticness, danceability, " \
                       "duration_ms, energy, instrumentalness, `key`, liveness, loudness, `mode`, speechiness, tempo, " \
                       "time_signature, valence, mood) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

        # Pass the values to the execute method
        mycursor.execute(insert_query, values)

# Commit all the changes
mydb.commit()
# close the connection to the database
mydb.close()