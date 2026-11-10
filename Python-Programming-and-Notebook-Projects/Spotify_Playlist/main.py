import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
from bs4 import BeautifulSoup

user = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
url = "https://www.billboard.com/charts/hot-100/2000-08-26"


response = requests.get(url=url, headers=header)
soup = BeautifulSoup(response.text, 'html.parser')

all_songs = soup.select("li ul li h3")
song_titles = [songs.getText().strip() for songs in all_songs]
# print(song_titles)

# 2
CLIENT_ID = "YOUR_CLIENT_ID"
CLIENT_SECRET = "YOUR_CLIENT_SECRET"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.text",
        username="smari",
    )
)
user_id = sp.current_user()["id"]
# print(user_id)


song_uris = []
year = user.split("-")[0]

import re

def clean_title(title):
    # Remove text inside parentheses and extra spaces
    return re.sub(r'\s*\(.*?\)', '', title).strip()

song_uris = []
year = user.split("-")[0]

for song in song_titles:
    clean_song = clean_title(song)
    query = f"track:{clean_song}"
    try:
        result = sp.search(q=query, type="track", limit=1)
        tracks = result["tracks"]["items"]
        if tracks:
            uri = tracks[0]["uri"]
            song_uris.append(uri)
        else:
            print(f"❌ Not found on Spotify: {song}")
    except Exception as e:
        print(f"⚠️ Error searching for '{song}': {e}")
        continue


playlist = sp.user_playlist_create(user=user_id, name=f"{user} Billboard 100", public=False)
print(playlist)

web_page = sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)