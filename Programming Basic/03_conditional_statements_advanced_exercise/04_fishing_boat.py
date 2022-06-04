budjet = int(input())
season = input()
fishermen_number = int(input())
costs = 0
if season == 'Spring':
    if 0 < fishermen_number <= 6:
        costs = 3000 - 3000 * 0.1
    elif 6 < fishermen_number <= 12:
        costs = 3000 - 3000 * 0.15
    else:
        costs = 3000 - 3000 * 0.25
elif season == 'Summer'or season == 'Autumn':
    if 0 < fishermen_number <= 6:
        costs = 4200 - 4200 * 0.1
    elif 6 < fishermen_number <= 12:
        costs = 4200 - 4200 * 0.15
    else:
        costs = 4200 - 4200 * 0.25
elif season == 'Winter':
    if 0 < fishermen_number <= 6:
        costs = 2600 - 2600 * 0.1
    elif 6 < fishermen_number <= 12:
        costs = 2600 - 2600 * 0.15
    else:
        costs = 2600 - 2600 * 0.25

if fishermen_number % 2 == 0 and (season != 'Autumn'):
    costs -= costs * 0.05

diff = abs(budjet - costs)
if budjet >= costs:
    print(f'Yes! You have {diff:.2f} leva left.')
else:
    print(f'Not enough money! You need {diff:.2f} leva.')