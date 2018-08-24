from player import Player
from utils import run_command


class SpotifyPlayer(Player):
    def get_status(self):
        state = run_command('playerctl', 'status')
        return state[:len(state)-1]

    def is_running(self):
        state = self.get_status()
        return state == 'Playing' or state == 'Paused'

    def is_paused(self):
        return self.get_status() == 'Paused'

    def toggle(self):
        run_command('playerctl', 'play-pause')

    def play(self):
        run_command('playerctl', 'play')

    def pause(self):
        run_command('playerctl', 'pause')

    def stop(self):
        run_command('playerctl', 'stop')

    def next(self):
        run_command('playerctl', 'next')

    def previous(self):
        run_command('playerctl', 'previous')

    def get_artist(self):
        return run_command('playerctl', 'metadata', 'artist')

    def get_title(self):
        return run_command('playerctl', 'metadata', 'title')
