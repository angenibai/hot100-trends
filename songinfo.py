import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

intToKey = {
    0:'C', 1:'C#/Db', 2:'D', 3:'D#/Eb', 4:'E', 5:'F', 6:'F#/Gb',
    7:'G', 8:'G#/Ab', 9:'A', 10:'A#/Bb', 11:'B', -1:'NA'
}

intToMode = {
    0:'minor', 1:'major'
}

birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

results = sp.artist_albums(birdy_uri, album_type='album')
albums = results['items']
while results['next']:
    results = sp.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])


