import datetime
import time
import os

def timer(min, msg, curr, sess):
    dt = datetime.datetime.now()
    it = datetime.timedelta(0, dt.second, dt.microsecond, 0, dt.minute, dt.hour, 0)
    ft = datetime.timedelta(0, dt.second, dt.microsecond, 0, dt.minute+min, dt.hour, 0)
    while (ft>it):
        os.system('clear')
        print(msg)
        dt = datetime.datetime.now()
        ct = datetime.timedelta(0, dt.second, dt.microsecond, 0, dt.minute, dt.hour, 0)
        print("Current Time: " + str(dt.hour) + ":" + str(dt.minute) + ":" + str(dt.second))
        print("Time Left: " + (str(ft-ct)).split(".")[0])
        print("Session: " + str(curr) + "/" + str(sess))
        time.sleep(1)

def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}" sound name "Default"'
              """.format(text, title))
