from math import ceil

serial_name = input()
serial_time = int(input())
break_time = int(input())
lunch_time = break_time / 8
rest_time = break_time / 4
time_left = break_time - lunch_time - rest_time
diff = ceil(abs(serial_time - time_left))
if time_left >= serial_time:
    print(f"You have enough time to watch {serial_name} and left with {diff} minutes free time.")
else:
    print(f"You don't have enough time to watch {serial_name}, you need {diff} more minutes.")