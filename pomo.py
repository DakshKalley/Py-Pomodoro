from timer import timer, notify
Study = int(input("Study Time: "))
Break = int(input("Break Time: "))
Sess = int(input("# of Sessions: "))

while Sess > 0:
    timer(Study, "~~ Study ~~")
    notify("Pomodoro", "Break Start")
    timer(Break, "~~ Break ~~")
    notify("Pomodoro", "Break Over")
    Sess -= 1

print("Study Session Complete!")
notify("Pomodoro", "Study Session Complete!")
