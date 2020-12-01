from timer import timer, notify
Work = int(input("Work Time: "))
Break = int(input("Break Time: "))
Sess = int(input("# of Sessions: "))
Current = 1
Total = Sess

while Sess > 0:
    timer(Work, "~~ Work ~~", Current, Total)
    notify("Pomodoro", "Break Start")
    timer(Break, "~~ Break ~~", Current, Total)
    notify("Pomodoro", "Break Over")
    Current += 1
    Sess -= 1

print("Pomodoro Sessions Complete!")
notify("Pomodoro", "Work Sessions Complete!")
