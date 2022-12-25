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


"""
from timer import timer, notify
Work = 50
Break = 10
Current = 1
Total = 1


timer(Work, "~~ Work ~~", Current, Total)
notify("Pomodoro", "Break Start")
timer(Break, "~~ Break ~~", Current, Total)
notify("Pomodoro", "Work Time")

print("Pomodoro Session Complete!")
notify("Pomodoro", "Work Session Complete!")


from timer import timer, notify
Work = int(input("Work Time: "))
Break = int(input("Break Time: "))
Sess = int(input("# of Sessions: "))
Current = 1
Total = Sess

while (Sess>0):
    timer(Work, "~~ Work ~~", Current, Total)
    notify("Pomodoro", "Break Start")
    timer(Break, "~~ Break ~~", Current, Total)
    notify("Pomodoro", "Break Over")
    Current += 1
    Sess -= 1
    
print("Pomodoro Sessions Complete!")
notify("Pomodoro", "Work Sessions Complete!")
"""