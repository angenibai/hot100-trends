import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import csv
import re

intToKey = {
    0:'C', 1:'C#/Db', 2:'D', 3:'D#/Eb', 4:'E', 5:'F', 6:'F#/Gb',
    7:'G', 8:'G#/Ab', 9:'A', 10:'A#/Bb', 11:'B', -1:'NA'
}

intToMode = {
    0:'minor', 1:'major'
}

# trackid: {title, artists, year, rank, tempo, time_signature, duration_ms, key, mode, acousticness, danceability, energy, instrumentalness, loudness, valence}
# note year is year of highest rank
tracks = {}
missing_tracks = {}

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

with open('missing.csv') as f:
    reader = csv.DictReader(f)
    count = 0
    for row in reader:
        if count > 5:
            break
        title = row['title']
        title.replace('"','')
        artist = row['artist']
        first = artist.split(' ')[0]

        query = 'track:' + title + ' artist:' + first
        query.replace(' ', '%20')

        

        count += 1