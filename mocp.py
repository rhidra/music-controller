from player import Player, run_command


class MocpPlayer(Player):
    def get_status(self):
        state = run_command('mocp', '-Q "%state"')
        return state[2:len(state)-2]

    def is_running(self):
        state = self.get_status()
        return state != 'STOP'

    def is_paused(self):
        return self.get_status() == 'PAUSE'

    def toggle(self):
        run_command('mocp', '-G')

    def play(self):
        run_command('mocp', '--unpause')

    def pause(self):
        run_command('mocp', '--pause')

    def stop(self):
        run_command('mocp', '--stop')

    def next(self):
        run_command('mocp', '--next')

    def previous(self):
        run_command('mocp', '--previous')

    def get_artist(self):
        s = run_command('mocp', '-Q', '"%artist"')
        return s[1:len(s)-2]

    def get_title(self):
        return run_command('mocp', '-Q', '%song')
