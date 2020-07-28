from timer import timer, notify
Work = int(input("Work Time: "))
Break = int(input("Break Time: "))
Sess = int(input("# of Sessions: "))

while Sess > 0:
    timer(Work, "~~ Work ~~")
    notify("Pomodoro", "Break Start")
    timer(Break, "~~ Break ~~")
    notify("Pomodoro", "Break Over")
    Sess -= 1

print("Pomodoro Sessions Complete!")
notify("Pomodoro", "Work Sessions Complete!")
