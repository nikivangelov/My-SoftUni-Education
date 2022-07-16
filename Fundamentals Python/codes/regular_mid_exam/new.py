command_list = input().split('||')
starting_fuel_amount = int(input())
starting_ammunition_amount = int(input())
current_ammunition = starting_ammunition_amount
current_fuel = starting_fuel_amount
for command in range(len(command_list)):
    current_command_list = command_list[command].split(' ')
    current_command = current_command_list[0]
    if current_command == 'Titan':
        print("You have reached Titan, all passengers are safe.")
        break

    if current_command == 'Enemy':
        enemy_s_armour = int(current_command_list[1])

        if current_ammunition >= enemy_s_armour:
            print(f"An enemy with {enemy_s_armour} armour is defeated.")
            current_ammunition -= enemy_s_armour
        else:
            if current_fuel >= enemy_s_armour * 2:
                print(f"An enemy with {enemy_s_armour} armour is outmaneuvered.")
            else:
                print("Mission failed.")
                break
    if current_command == 'Repair':
        number_of_ammunition_and_fuel_added = int(current_command_list[1])
        current_fuel += number_of_ammunition_and_fuel_added
        current_ammunition += number_of_ammunition_and_fuel_added * 2
        print(f"Ammunitions added: {number_of_ammunition_and_fuel_added * 2}.")
        print(f"Fuel added: {number_of_ammunition_and_fuel_added}.")

    if current_command == 'Travel':
        light_years = int(current_command_list[1])
        if current_fuel <= 0:
            print("Mission failed.")
            break
        else:
            print(f"The spaceship travelled {light_years} light-years.")
