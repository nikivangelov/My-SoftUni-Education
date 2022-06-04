location_number = int(input())

for i in range(1, location_number + 1):
    gold_on_location = 0
    average_gold_per_day = 0
    expected_gold = int(input())
    period_of_digging = int(input())
    for j in range(1, period_of_digging + 1):
        gold_per_day = int(input())
        gold_on_location += gold_per_day

    average_gold_per_day = gold_on_location / period_of_digging
    diff = abs(average_gold_per_day - expected_gold)
    if average_gold_per_day >= expected_gold:
        print(f'Good job! Average gold per day: {average_gold_per_day:.2f}.')
    else:
        print(f'You need {diff:.2f} gold.')