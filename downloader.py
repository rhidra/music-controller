from utils import run_command

class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def __repr__(self):
        return '%s - %s' % (self.artist, self.title)


def get_song():
    path = '/home/rhidra/music_list.txt'
    with open(path) as file:
        line = file.readline()
    title, artist = line.replace('\n', '').split(' - ')
    return Song(title=title, artist=artist)
