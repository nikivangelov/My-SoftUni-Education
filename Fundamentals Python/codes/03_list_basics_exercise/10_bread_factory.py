event_list = input().split('|')
energy_amount = 100
coin_amount = 100
current_energy = energy_amount
day_completed_condition = True

for event in event_list:
    current_event_list = event.split('-')
    event_name = current_event_list[0]
    event_value = int(current_event_list[1])
    gained_energy = 0
    if event_name == 'rest':
        current_energy += event_value
        if current_energy >= 100:
            gained_energy = 100 - current_energy + event_value
            current_energy = 100
        else:
            gained_energy = event_value
        print(f'You gained {gained_energy} energy.')
        print(f'Current energy: {current_energy}.')
        continue
    if event_name == 'order':
        if current_energy >= 30:
            current_energy -= 30
            coin_amount += event_value
            print(f'You earned {event_value} coins.')
        else:
            current_energy += 50
            print('You had to rest!')
        continue

    if coin_amount >= event_value:
        coin_amount -= event_value
        print(f'You bought {event_name}.')
    else:
        print(f'Closed! Cannot afford {event_name}.')
        day_completed_condition = False
        break

if day_completed_condition:
    print('Day completed!')
    print(f'Coins: {coin_amount}')
    print(f'Energy: {current_energy}')



