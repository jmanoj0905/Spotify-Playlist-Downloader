from pytube import YouTube
import pywhatkit as pwt
from youtubesearchpython import VideosSearch
import csv

def main():
    with open("final.csv","r",encoding='utf-8') as file:
        lines=csv.reader(file)
        next(lines)
        for i in lines:
            song_name=i[0]
            artist_name=i[1]

            SongSearch = VideosSearch(song_name+artist_name, limit = 1)
            data = SongSearch.result()
            video_links = [item['link'] for item in data['result'] if item['type'] == 'video']

            video = YouTube(str(video_links))
            video = video.streams.get_lowest_resolution()
            video.download(str("Songs"))

if __name__ == "__main__":
    main()