stadium_capacity = int(input())
all_fans = int(input())
fans_in_A = 0
fans_in_B = 0
fans_in_V = 0
fans_in_G = 0
total_fans = fans_in_A + fans_in_B + fans_in_V + fans_in_G
for _ in range(1, all_fans + 1):
    stand = input()
    if stand == 'A':
        fans_in_A += 1
    elif stand == 'B':
        fans_in_B += 1
    elif stand == 'V':
        fans_in_V += 1
    elif stand == 'G':
        fans_in_G += 1

print(f'{fans_in_A / all_fans * 100:.2f}%')
print(f'{fans_in_B / all_fans * 100:.2f}%')
print(f'{fans_in_V / all_fans * 100:.2f}%')
print(f'{fans_in_G / all_fans * 100:.2f}%')
print(f'{all_fans / stadium_capacity * 100 :.2f}%')