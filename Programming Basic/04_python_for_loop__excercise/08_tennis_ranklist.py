from math import floor

num_of_tournaments = int(input())
starting_points = int(input())
total_points = starting_points
count_wins = 0
points_sf = 0
points_f = 0
points_w = 0
for i in range(1, num_of_tournaments + 1):
    stage = input()
    if stage == 'SF':
        total_points += 720
        points_sf += 720
    elif stage == 'F':
        total_points += 1200
        points_f += 1200
    elif stage == 'W':
        total_points += 2000
        points_w += 2000
        count_wins += 1

print(f'Final points: {total_points}')
print(f'Average points: {floor((points_sf + points_f + points_w) / num_of_tournaments)}')
print(f'{(count_wins / num_of_tournaments * 100):.2f}%')

