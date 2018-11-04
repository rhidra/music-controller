#!/usr/bin/python3

from deadbeef import DeadbeefPlayer
from spotify import SpotifyPlayer
from mocp import MocpPlayer
from youtube import YoutubePlayer
from player import Player
from utils import notif
import sys


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: player_control.py <next | prev | stop | toggle | status | artist | title>")
        exit()
    elif sys.argv[1] not in ["next", "prev", "stop", "toggle", "status", "artist", "title"]:
        print("Usage: player_control.py <next | prev | stop | toggle | status | artist | title>")
        exit()

    action = str(sys.argv[1])

    player = Player()

    if SpotifyPlayer().is_playing():
        player = SpotifyPlayer()
    elif DeadbeefPlayer().is_playing():
        player = DeadbeefPlayer()
    elif MocpPlayer().is_playing():
        player = MocpPlayer()
    elif SpotifyPlayer().is_running():
        player = SpotifyPlayer()
    elif DeadbeefPlayer().is_running():
        player = DeadbeefPlayer()
    elif MocpPlayer().is_running():
        player = MocpPlayer()
    elif YoutubePlayer().is_running():
        player = YoutubePlayer()
    elif action != "status":
        notif("Aucun lecteur n\'est activé !")

    if action == "next":
        player.next()
    elif action == "prev":
        player.previous()
    elif action == "stop":
        player.stop()
    elif action == "toggle":
        player.toggle()
    elif action == "status":
        print(player)
    elif action == "artist":
        print(player.get_song().artist, end='')
    elif action == "title":
        print(player.get_song().title, end='')
