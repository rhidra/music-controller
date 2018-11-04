import sys
import os
import subprocess
from utils import notif, run_command, Song


class Player():
    def is_running(self):
        return False

    def is_playing(self):
        return not self.is_paused() and self.is_running()
    
    def __repr__(self):
        if self.is_running():
            if self.is_paused():
                return "  {}".format(self.get_song())
            else:
                return "  {}".format(self.get_song())
        else:
            return "Nothing running :("

    def get_song(self):
        return Song(self.get_title(), self.get_artist())
