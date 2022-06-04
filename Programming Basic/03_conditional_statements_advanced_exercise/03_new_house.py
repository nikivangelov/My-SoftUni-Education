flower_kind = input()
flower_number = int(input())
budjet = int(input())
costs = 0
price = 0
if flower_kind == 'Roses':
    costs = flower_number * 5
    if flower_number > 80:
        costs -= costs * 0.1
elif flower_kind == 'Dahlias':
    costs = flower_number * 3.8
    if flower_number > 90:
        costs -= costs * 0.15
elif flower_kind == 'Tulips':
    costs = flower_number * 2.8
    if flower_number > 80:
        costs -= costs * 0.15
elif flower_kind == 'Narcissus':
    costs = flower_number * 3
    if flower_number < 120:
        costs += costs * 0.15
elif flower_kind == 'Gladiolus':
    costs = flower_number * 2.5
    if flower_number < 80:
        costs += costs * 0.2

diff = abs(budjet - costs)
if budjet >= costs:
    print(f'Hey, you have a great garden with {flower_number} {flower_kind} and {diff:.2f} leva left.')
else:
    print(f'Not enough money, you need {diff:.2f} leva more.')