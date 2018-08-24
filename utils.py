import sys
import os
import subprocess


def run_command(*cmd):
    r = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    s = r.stdout.decode('utf-8')
    return s


def notif(s):
    os.system('notify-send "Player Controller" "{}"'.format(s))
