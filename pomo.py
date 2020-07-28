import datetime
import time
import os

Study = int(input("Study Time: "))
Break = int(input("Break Time: "))
Sess = int(input("# of Sessions: "))

def timer(min, msg):
    sec = (min*60)
    while (sec) > 0:
        os.system('clear')
        print(msg)
        dt = datetime.datetime.now()
        print("Current Time: " + str(dt.hour) + ":" + str(dt.minute) + ":" + str(dt.second) + "\n" + str(sec))
        time.sleep(1)
        sec -= 1

def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}" sound name "Default"'
              """.format(text, title))

while Sess > 0:
    timer(Study, "~~ Study ~~")
    notify("Pomodoro", "Break Start")
    timer(Break, "~~ Break ~~")
    notify("Pomodoro", "Break Over")
    Sess -= 1
print("Study Session Complete!")
