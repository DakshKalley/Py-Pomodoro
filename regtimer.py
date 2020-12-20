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
