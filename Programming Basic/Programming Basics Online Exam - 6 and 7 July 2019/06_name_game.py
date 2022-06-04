
max_points = 0
winner = ''
while True:
    player_name = input()
    if player_name == 'Stop':
        break
    points = 0
    for n in range(0, len(player_name)):
        number = int(input())
        if number == ord(player_name[n]):
            points += 10
        else:
            points += 2

    if points >= max_points:
        max_points = points
        winner = player_name

print(f'The winner is {winner} with {max_points} points!')