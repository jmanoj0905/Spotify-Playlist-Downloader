from pytube import YouTube
from youtubesearchpython import VideosSearch
import csv

from tkinter import messagebox

def main():
    with open("songlist.csv", "r", encoding='utf-8') as file:
        lines = csv.reader(file)
        next(lines)
        for i in lines:
            song_name = i[0]
            artist_name = i[1]

            SongSearch = VideosSearch(song_name + artist_name, limit=1)
            data = SongSearch.result()

            if 'result' not in data or not data['result']:
                messagebox.showerror("Error", f"No results found for {song_name} by {artist_name}")
                continue

            video_links = [item['link'] for item in data['result'] if item['type'] == 'video']

            try:
                video = YouTube(str(video_links[0]))
                video = video.streams.get_lowest_resolution()
                video.download(str("Songs"))
            except Exception as e:
                if 'age restricted' in str(e).lower():
                    messagebox.showerror("Error", f"{song_name} by {artist_name} is age restricted.")
                else:
                    messagebox.showerror("Error", f"An error occurred while downloading {song_name} by {artist_name}: {str(e)}")

if __name__ == "__main__":
    main()
