hour, minutes = int(input()), int(input())
hour_in_minutes = hour * 60
time_in_minutes = hour_in_minutes + minutes + 15
hour_output = time_in_minutes // 60
minutes_output = time_in_minutes % 60
if hour_output > 23:
    print(f'0:{minutes_output:02d}')
else:
    print(f'{hour_output}:{minutes_output:02d}')
