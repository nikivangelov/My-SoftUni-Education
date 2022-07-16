days_of_adventure = int(input())
number_of_players = int(input())
group_energy = float(input())
water_per_day_per_person = float(input())
total_water_amount = number_of_players * water_per_day_per_person * days_of_adventure
food_per_day_per_person = float(input())
total_food_amount = food_per_day_per_person * number_of_players * days_of_adventure
run_out_of_energy = False

for current_day in range(1, days_of_adventure + 1):
    energy_loss_per_day = float(input())
    group_energy -= energy_loss_per_day

    if group_energy <= 0:
        run_out_of_energy = True
        break

    if current_day % 2 == 0:
        group_energy *= 1.05
        total_water_amount *= 0.7
    if current_day % 3 == 0:
        total_food_amount -= total_food_amount / number_of_players
        group_energy *= 1.1

if run_out_of_energy:
    print(f'You will run out of energy. You will be left with {total_food_amount:.2f} food and '
          f'{total_water_amount:.2f} water.')
else:
    print(f'You are ready for the quest. You will be left with - {group_energy:.2f} energy!')

