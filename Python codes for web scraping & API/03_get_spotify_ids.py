'''
This gets matching spotify track id and spotify artist id using isrc to search in Spotify API. When no matching isrc
is returned, use artist name + track name to form the query to search using Spotify API.
'''

import csv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from config import client_id, client_secret

def get_spotify_id(input_file_path, output_file_path):

    # Set up the Spotify API client
    auth_manager = SpotifyClientCredentials(client_id = client_id, client_secret = client_secret)
    sp = spotipy.Spotify(auth_manager = auth_manager)

    # read the input csv file
    with open(input_file_path, 'r') as input_file:
        reader = csv.DictReader(input_file)

        # Open the output CSV file for writing
        with open(output_file_path, 'w', newline='', encoding='utf-8') as output_file:
            content = csv.writer(output_file)
            column_names = ['isrc', 'artist', 'artist_id', 'track_name', 'track_spotify_id']
            content.writerow(column_names)

            # Loop through each row from the input CSV file to get isrc, track_name and artist_name
            for row in reader:
                isrc = row['isrc']
                track_name = row['title']
                artist_name = row['artist']

                # Search for the artist and track by using isrc number
                query = f'isrc:{isrc}'
                results = sp.search(q=query, type='track')

                if len(results['tracks']['items']) > 0:
                   track_spotify_id = results['tracks']['items'][0]['id']
                   artist_id = results['tracks']['items'][0]['artists'][0]['id']
                   content.writerow([isrc, artist_name, artist_id, track_name, track_spotify_id])

                # if using isrc does not return any result, use a new query using the artist name and track name to search
                else:
                   new_query = f'artist: {artist_name}%20track: {track_name}'
                   new_results = sp.search(q=new_query, type='track')

                   if len(new_results['tracks']['items']) > 0:
                       # row['artist_id'] = new_results['tracks']['items'][0]['artists'][0]['id']
                       new_artist_id = new_results['tracks']['items'][0]['artists'][0]['id']
                       # row['track_spotify_id'] = new_results['tracks']['items'][0]['id']
                       new_track_spotify_id = new_results['tracks']['items'][0]['id']
                       content.writerow([isrc, artist_name, new_artist_id, track_name, new_track_spotify_id])
                   else:
                       # if there is still no match, return empty strings for artist_id and spotify_track_id
                       content.writerow([row['isrc'], artist_name, '', track_name, ''])

if __name__ == '__main__':
    get_spotify_id(input_file_path = 'unique_isrc.csv', output_file_path = 'isrc_spotify_ids.csv')