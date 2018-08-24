#!/usr/bin/python3

from deadbeef import DeadbeefPlayer
from spotify import SpotifyPlayer
from mocp import MocpPlayer
from player import Player
from utils import notif
import sys


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: player_control.py <next | prev | stop | toggle | status>")
        exit()
    elif sys.argv[1] not in ["next", "prev", "stop", "toggle", "status"]:
        print("Usage: player_control.py <next | prev | stop | toggle | status>")
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
