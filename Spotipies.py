import csv
import re
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from tkinter import messagebox

def URLGET(link):
    global playlist_link
    playlist_link = link

def main():
    with open(r"credentials.txt") as f:
        [SPOTIPY_CLIENT_ID,SPOTIPY_CLIENT_SECRET] = f.read().split("\n")
        f.close()

    auth_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID,client_secret=SPOTIPY_CLIENT_SECRET)
    session = spotipy.Spotify(auth_manager=auth_manager)

    if match := re.match(r"https://open.spotify.com/playlist/(.*)\?", playlist_link):
        playlist_uri = match.groups()[0]
    else:
        messagebox.showerror("Error", "Expected format: https://open.spotify.com/playlist/")
        raise ValueError("Expected format: https://open.spotify.com/playlist/...")
        

    tracks = session.playlist_tracks(playlist_uri)["items"]

    with open('songlist.csv','w',encoding='utf-8',newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['tracks','artist'])
        for track in tracks:
            name = track['track']['name']
            artists = ', '.join(
                [artist['name'] for artist in track['track']['artists']]
            )
            writer.writerow([name,artists])

if __name__ == "__main__":
    main()
    