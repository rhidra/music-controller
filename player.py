import sys
import os
import subprocess


def run_command(*cmd):
    r = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    s = r.stdout.decode('utf-8')
    return s


def notif(s):
    os.system('notify-send "Player Controller" "{}"'.format(s))


class Player():
    def is_running(self):
        return False
    def is_playing(self):
        return not self.is_paused() and self.is_running()
    def __repr__(self):
        if self.is_running():
            if self.is_paused():
                return "  {} - {}".format(self.get_artist(), self.get_title())
            else:
                return "  {} - {}".format(self.get_artist(), self.get_title())
        else:
            return "Nothing running :("
