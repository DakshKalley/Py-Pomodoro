import datetime
import time
import os

Study = int(input("Study Time: "))
Break = int(input("Break Time: "))
Sessions = int(input("# of Sessions: "))

def timer(min, msg):
    sec = (min)
    while (sec) > 0:
        os.system('clear')
        print(msg)
        dt = datetime.datetime.now()
        pt = datetime.datetime()
        print("Current Time: " + str(dt.hour) + ":" + str(dt.minute) + ":" + str(dt.second) + "\n" + str(sec))
        time.sleep(1)
        sec -= 1

while Sessions > 0:
    timer(Study, "~~ Study ~~")
    timer(Study, "~~ Break ~~")
    Sessions -= 1
print("Study Session Complete!")
