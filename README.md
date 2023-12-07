# Spotify Playlist Downloader
# SpotiDownloader

![GitHub last commit](https://img.shields.io/github/last-commit/your-username/spotify-playlist-downloader)
![GitHub license](https://img.shields.io/github/license/your-username/spotify-playlist-downloader)
![GitHub stars](https://img.shields.io/github/stars/your-username/spotify-playlist-downloader?style=social)

## Overview

This is a comprehensive Spotify playlist downloader that allows users to download their favorite Spotify playlists locally. The project consists of a Tkinter GUI for user interaction, Spotipy for Spotify API interaction, a web scraping program to fetch song details, and tools to download and convert music.

## Features

- **User-Friendly GUI:** Utilizes Tkinter for a graphical interface, making it easy for users to input the Spotify playlist link and local storage location.

- **Spotify API Integration:** Uses the Spotipy module to interact with the Spotify API, fetching the list of songs and artist names from the given playlist.

- **CSV Generation:** Creates a CSV file containing the details of songs and artists obtained from the Spotify API response.

- **Web Scraping:** Utilizes web scraping to download music from YouTube based on the information stored in the CSV file.

- **Conversion to MP3:** Converts downloaded music from MP4 to MP3 format using a dedicated script.

## Prerequisites

- Python 3.x
- Install dependencies
  
  ```bash
  pip install -r requirements.txt

## Installation

1. Clone the repository:

```bash
git clone https://github.com/jmanoj0905/SpotiDownloader.git
cd SpotiDownloader
```

2.Run the Tkinter GUI:

python dagui.py

- **Enter the Spotify playlist link and local storage location.**

- **Click on the "Download" button to initiate the process.**

- **The program will fetch the playlist details, create a CSV file, download music, and convert it to MP3.**
