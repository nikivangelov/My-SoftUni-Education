holidays = int(input())
working_days = 365 - holidays
working_day_play = working_days * 63
holiday_play = holidays * 127
total_minutes_play = working_day_play + holiday_play
diff = abs(total_minutes_play - 30000)
H = diff // 60
M = diff % 60
if total_minutes_play > 30000:
    print('Tom will run away')
    print(f'{H} hours and {M:02d} minutes more for play')
else:
    print('Tom sleeps well')
    print(f'{H} hours and {M:02d} minutes less for play')