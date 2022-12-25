import argparse
import time
import os

parser = argparse.ArgumentParser(description='Pomodoro timer')
parser.add_argument('duration', type=int, help='duration of the Pomodoro in minutes')
parser.add_argument('pause', type=int, help='duration of the break in minutes')
parser.add_argument('-t', '--task', help='task name')
args = parser.parse_args()

duration = args.duration * 60  # Convert minutes to seconds
pause = args.pause * 60

#Pomodoro Timer
print(f'Starting Pomodoro for {duration // 60} minutes')
for i in range(duration, 0, -1):
    minutes, seconds = divmod(i, 60)
    print(f'{minutes:02d}:{seconds:02d}', end='\r')
    time.sleep(1)

print('\a')
if args.task:
    message = f'Pomodoro completed: {args.task}'
else:
    message = 'Pomodoro completed'

os.system(f'osascript -e \'display notification "{message}" with title "Pomodoro Timer"\'')

#Break Timer
print(f'Starting break for {pause // 60} minutes')
for i in range(duration, 0, -1):
    minutes, seconds = divmod(i, 60)
    print(f'{minutes:02d}:{seconds:02d}', end='\r')
    time.sleep(1)

print('\a')
message = 'Break completed'

os.system(f'osascript -e \'display notification "{message}" with title "Pomodoro Timer" sound name "Default"\'')