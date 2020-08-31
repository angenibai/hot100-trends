import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
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

# from 1959
YEAR_START = 2019
YEAR_END = 2020

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

for year in range(YEAR_START, YEAR_END):
    file_path = 'hot100files/' + str(year) + '.csv'
    with open(file_path, mode='r') as f:
        reader = csv.DictReader(f)

        track_ids_year = []
        line_count = 0
        for row in reader:

            if line_count >= 5:
                break
            
            # construct query to search for the track id
            query = 'track:' + row["Title"] + 'artist:' + row["Artists Separately"]
            query.replace(' ', '%20')
            results = sp.search(q=query, limit=1, type='track')

            items = results['tracks']['items']
            if len(items) < 1:
                print(row["Title"], "no results found")
                missing_tracks[line_count] = {
                    'title':row["Title"],
                    'artists':row["Artist(s)"]
                    }
                line_count += 1
                continue
            if items[0]['type'] != 'track':
                print("Found type", items[0]['type'])
                missing_tracks[line_count] = {
                    'title':row["Title"],
                    'artists':row["Artist(s)"]
                    }
                line_count += 1
                continue
            track_id = items[0]['id']
            track_ids_year.append(track_id)
            # print(row["Title"], track_id) # ! DEBUG

            if track_id not in tracks:
                tracks[track_id] = {
                    'title':row["Title"],
                    'artists':row["Artist(s)"],
                    'year':year,
                    'rank':row["Rank"]
                }
            elif row["Rank"] < tracks[track_id]['rank']:
                    tracks[track_id]['rank'] = row["Rank"]
                    tracks[track_id]['year'] = year

            line_count += 1

    all_audio_features = sp.audio_features(track_ids_year)
    for info in all_audio_features:
        track_id = info['id']
        tracks[track_id]['id'] = track_id;
        tracks[track_id]['uri'] = info['uri']
        tracks[track_id]['danceability'] = info['danceability']
        tracks[track_id]['energy'] = info['energy']
        tracks[track_id]['key'] = intToKey[info['key']]
        tracks[track_id]['loudness'] = info['loudness']
        tracks[track_id]['mode'] = intToMode[info['mode']]
        tracks[track_id]['acousticness'] = info['acousticness']
        tracks[track_id]['instrumentalness'] = info['instrumentalness']
        tracks[track_id]['valence'] = info['valence']
        tracks[track_id]['tempo'] = info['tempo']
        tracks[track_id]['time_signature'] = info['time_signature']
        tracks[track_id]['duration_ms'] = info['duration_ms']

    #print(tracks)
    # all_audio_features = json.load(all_audio_features)

# save all data into a master doc
with open('master_doc.csv', mode='w') as f:
    fieldnames = ['id', 'uri', 'title', 'artists', 'year', 'rank', 'tempo', 'time_signature', 'duration_ms', 'key', 'mode', 'acousticness', 'danceability', 'energy', 'instrumentalness', 'loudness', 'valence']
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()
    for k in tracks.keys():
        writer.writerow(tracks[k])


# save the missing ones as well
with open('missing.csv', mode='w') as f:
    fieldnames = ['title', 'artists']
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()
    for k in missing_tracks.keys():
        writer.writerow(tracks[k])
