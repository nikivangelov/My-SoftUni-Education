club_name = input()
matchdays = int(input())
points = 0
wins_counter = 0
draws_counter = 0
losses_counter = 0

if matchdays == 0:
    print(f"{club_name} hasn't played any games during this season.")
else:
    for _ in range(1, matchdays + 1):
        result = input()
        if result == 'W':
            wins_counter += 1
            points += 3
        elif result == 'D':
            draws_counter += 1
            points += 1
        elif result == 'L':
            losses_counter += 1

    print(f'{club_name} has won {points} points during this season.')
    print('Total stats:')
    print(f'## W: {wins_counter}')
    print(f'## D: {draws_counter}')
    print(f'## L: {losses_counter}')
    print(f'Win rate: {wins_counter / matchdays * 100 :.2f}%')