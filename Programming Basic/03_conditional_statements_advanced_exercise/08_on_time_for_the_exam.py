hours_of_exam = int(input())
minutes_of_exam = int(input())
hours_of_arrival = int(input())
minutes_of_arrival = int(input())
arrival_time = hours_of_arrival * 60 + minutes_of_arrival
exam_time = hours_of_exam * 60 + minutes_of_exam
diff = abs(arrival_time - exam_time)
hour = diff // 60
minutes = diff % 60
if exam_time < arrival_time and diff < 60:
    print('Late')
    print(f'{minutes} minutes after the start')
elif exam_time < arrival_time and diff >= 60:
    print('Late')
    print(f'{hour}:{minutes:02d} hours after the start')
elif exam_time >= arrival_time and diff <= 30:
    print('On time')
    print(f'{minutes} minutes before the start')
elif exam_time > arrival_time and diff > 30:
    print('Early')
    if 30 < diff < 60:
        print(f'{minutes} minutes before the start')
    elif diff >= 60:
        print(f'{hour}:{minutes:02d} hours before the start')