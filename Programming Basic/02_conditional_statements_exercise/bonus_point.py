starting_points = int(input())
bonus_points = 0

if 0 <= starting_points <= 100:
    bonus_points += 5
elif 100 < starting_points <= 1000:
    bonus_points += starting_points * 0.20
elif starting_points > 1000:
    bonus_points += starting_points * 0.10

if starting_points % 2 == 0:
    bonus_points += 1
elif starting_points % 10 == 5:
    bonus_points += 2

total_points = starting_points + bonus_points
print(bonus_points)
print(total_points)
