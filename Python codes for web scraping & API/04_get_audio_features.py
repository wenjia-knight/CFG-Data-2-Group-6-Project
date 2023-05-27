'''
use this to extract a track's audio features.
'''
import csv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from config import client_id, client_secret

def get_audio_feature(input_file_path, output_file_path):

    # Set up the Spotify API client
    auth_manager = SpotifyClientCredentials(client_id = client_id, client_secret = client_secret)
    sp = spotipy.Spotify(auth_manager = auth_manager)

    # read the input csv file
    with open(input_file_path, 'r') as input_file:
        reader = csv.DictReader(input_file)

        # Open the output CSV file for writing
        with open(output_file_path, 'w', newline='', encoding='utf-8') as output_file:
            content = csv.writer(output_file)
            column_names = ['isrc', 'track_name', 'track_spotify_id', 'acousticness', 'danceability', 'duration_ms', 'energy',
                            'instrumentalness', 'key', 'liveness', 'loudness', 'mode', 'speechiness', 'tempo', 'time_signature', 'valence']
            content.writerow(column_names)

            # Loop through each row from the input CSV file
            for row in reader:
                track_name = row['track_name']
                track_id = row['track_spotify_id']
                isrc = row['isrc']

                # Search for a track's audio features using track spotify id
                track_audio_features = sp.audio_features(track_id)[0]

                acousticness = track_audio_features['acousticness']
                danceability = track_audio_features['danceability']
                duration_ms = track_audio_features['duration_ms']
                energy = track_audio_features['energy']
                instrumentalness = track_audio_features['instrumentalness']
                key = track_audio_features['key']
                liveness = track_audio_features['liveness']
                loudness = track_audio_features['loudness']
                mode = track_audio_features['mode']
                speechiness = track_audio_features['speechiness']
                tempo = track_audio_features['tempo']
                time_signature = track_audio_features['time_signature']
                valence = track_audio_features['valence']

                content.writerow([isrc, track_name, track_id, acousticness, danceability, duration_ms, energy, instrumentalness,
                                  key, liveness, loudness, mode, speechiness, tempo, time_signature, valence])

if __name__ == '__main__':
    get_audio_feature(input_file_path = '../datasets/isrc_spotify_ids.csv', output_file_path = '../datasets/track_audio_features.csv')