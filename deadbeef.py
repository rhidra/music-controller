from player import Player, run_command


class DeadbeefPlayer(Player):
    def get_status(self):
        if run_command('deadbeef', '--nowplaying-tf', '%isplaying%') == '1':
            state = 'PLAY'
        elif run_command('deadbeef', '--nowplaying-tf', '%ispaused%') == '1':
            state = 'PAUSE'
        else:
            state = 'STOP'
        return state

    def is_running(self):
        state = self.get_status()
        return state != 'STOP'

    def is_paused(self):
        return self.get_status() == 'PAUSE'

    def toggle(self):
        run_command('deadbeef', '--play-pause')

    def play(self):
        run_command('deadbeef', '--play')

    def pause(self):
        run_command('deadbeef', '--pause')

    def stop(self):
        run_command('deadbeef', '--stop')

    def next(self):
        run_command('deadbeef', '--next')

    def previous(self):
        run_command('deadbeef', '--prev')

    def get_artist(self):
        return run_command('deadbeef', '--nowplaying-tf', '%artist%')

    def get_title(self):
        return run_command('deadbeef', '--nowplaying-tf', '%title%')
