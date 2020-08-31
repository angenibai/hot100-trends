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

with open('missing_1.csv') as f:
    reader = csv.DictReader(f)

    for row in reader:
        title = row['title']
        title.replace('"','')
        artist = row['artist']
        first = artist.split(' ')[0]

        query = 'track:' + title + ' artist:'