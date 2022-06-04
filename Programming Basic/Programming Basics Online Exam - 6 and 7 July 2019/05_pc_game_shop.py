n = int(input())
total_game_counter = 0
hearthstone_counter = 0
fornite_counter = 0
overwatch_counter = 0
others_counter = 0
for _ in range(1, n+1):
    game_name = input()
    total_game_counter += 1
    if game_name == 'Hearthstone':
        hearthstone_counter += 1
    elif game_name == 'Fornite':
        fornite_counter += 1
    elif game_name == 'Overwatch':
        overwatch_counter += 1
    else:
        others_counter += 1

print(f'Hearthstone - {hearthstone_counter / total_game_counter * 100:.2f}%')
print(f'Fornite - {fornite_counter / total_game_counter * 100:.2f}%')
print(f'Overwatch - {overwatch_counter / total_game_counter * 100:.2f}%')
print(f'Others - {others_counter / total_game_counter * 100:.2f}%')

