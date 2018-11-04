from utils import run_command, Song
import requests
import os
import re
import youtube_dl
import json
from bs4 import BeautifulSoup


def get_song():
    path = '/home/rhidra/music_list.txt'
    with open(path) as file:
        line = file.readline()
    data = json.loads(line)
    return Song(title=data[0], artist=data[1])


def get_yt_url(song):
    query = "%s %s" % (song.artist, song.title)
    r = requests.get('https://www.youtube.com/results', params={'search_query': query})
    soup = BeautifulSoup(r.text, 'lxml')
    for result in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
        if not "googleads" in result['href']:
            break
    return 'https://www.youtube.com' + result['href']


def download(url, song):
    print('Downloading %s for %s' % (url, song))
    while True:
        #try:
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                }],
                'outtmpl': 'Musique/{}.%(ext)s'.format(song),
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            break
        #except URLError:
        #    print('Erreur de téléchargement !!!! Restarting ...')


def get_yt_title(url):
    return run_command('youtube-dl', url, '-e')[:-1]

def download_file():
    path = '/home/rhidra/music_list.txt'
    with open(path) as file:
        for line in file:
            data = json.loads(line)
            song = Song(title=data[0], artist=data[1])
            url = get_yt_url(song)
            #user_in = input('Télécharger {} pour {} ? [O/N] '.format(get_yt_title(url), song))
            #if user_in == 'O' or user_in == 'o' or user_in == 'y' or  user_in == 'Y':
            download(url, song)

download_file()
