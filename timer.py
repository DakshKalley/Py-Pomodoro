import datetime
import time
import os

def convsec(seconds):
    seconds = seconds % (24 * 3600)
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return ("%d:%02d" % (minutes, seconds))


def timer(min, msg, curr, sess):
    sec = (min*60)
    while (sec) > 0:
        os.system('clear')
        print(msg)
        dt = datetime.datetime.now()
        print("Current Time: " + str(dt.hour) + ":" + str(dt.minute) + ":" + str(dt.second))
        print("Pomodoro Timer: " + str(convsec(sec)))
        print("Session: " + str(curr) + "/" + str(sess))
        time.sleep(1)
        sec -= 1

def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}" sound name "Default"'
              """.format(text, title))
