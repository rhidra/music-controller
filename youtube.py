from player import Player
from utils import run_command, notif
from functools import reduce
import os, json, lz4.block, youtube_dl



class YoutubePlayer(Player):
    msg = "Impossible de modifier l'état du player Youtube !"

    def is_running(self):
        return bool(len(self.get_yt_tabs()[0]))

    def is_paused(self):
        return not self.is_running()

    def toggle(self):
        notif(self.msg)

    def play(self):
        notif(self.msg)

    def pause(self):
        notif(self.msg)

    def stop(self):
        notif(self.msg)

    def next(self):
        notif(self.msg)

    def previous(self):
        notif(self.msg)

    def __repr__(self):
        url = self.get_url_playing()
        if not url:
            return "Nothing running in YT :("
        with youtube_dl.YoutubeDL({'quiet': True}) as ydl:
            return ydl.extract_info(url, download=False)['title']

    def get_artist(self):
        title = self.__repr__()
        t = title.split(' - ')
        return None if len(t) == 1 else t[0]

    def get_title(self):
        title = self.__repr__()
        t = title.split(' - ')
        return None if len(t) == 1 else reduce(lambda a, b: a+' - '+b, t[1:])

    def get_urls_open(self):
        with open('/home/rhidra/.mozilla/firefox/uzqthl8l.default-1527929644807/sessionstore-backups/recovery.jsonlz4', 'rb') as f:
            f.read(8)
            jdata = json.loads(lz4.block.decompress(f.read()).decode("utf-8"))
            tabs = [tab.get('entries')[tab.get('index')-1].get('url')
                        for win in jdata.get('windows')
                            for tab in win.get('tabs')]
            return (tabs, tabs[jdata["windows"][0]["selected"]-1])

    def get_yt_tabs(self):
        urls, current = self.get_urls_open()
        prefix = 'https://www.youtube.com/watch'
        return (list(filter(lambda url: prefix in url, urls)), current if prefix in current else None)

    def get_url_playing(self):
        tabs, current = self.get_yt_tabs()
        return tabs[0] if len(tabs)==1 else current if current else None
