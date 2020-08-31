# hot100-trends
Playing around with the Spotify API. Maybe finding interesting trends in the Billboard Year End Hot 100 for 1959-present.

## Setup
### Install dependencies
Install all dependencies from Pipfile:
```
pipenv install
```

If there are any errors, launch a virtual shell to use for running the programs:
```
pipenv shell
```

### Spotify credentials
Sign up for a Spotify Developer account and create a new app. Then, create a file named **.env** in the working directory.

In the **.env** file, create two new environment variables: **SPOTIPY_CLIENT_ID** and **SPOTIPY_CLIENT_SECRET**. Assign them to the Client ID and Client Secret ID found in your Spotify app. The file should look like this:
```
SPOTIPY_CLIENT_ID='abcde123456789'
SPOTIPY_CLIENT_SECRET='123456789abcde'
```


## Future steps
1. Storing all of the data in a masterdoc.csv
2. Visualising data in Tableau
3. Presenting data visualisation in a website
4. Creating an interactive website to explore data
