import sys
import os
import subprocess


def run_command(*cmd):
    r = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    s = r.stdout.decode('utf-8')
    return s


def notif(s):
    os.system('notify-send "Player Controller" "{}"'.format(s))


class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def __repr__(self):
        if self.artist and self.title:
            return '%s - %s' % (self.artist, self.title)
        elif self.title:
            return '%s' % self.title
        elif self.artist:
            return '%s' % self.artist
        else:
            return 'Unknown :('
