from math import ceil

number_of_people = int(input())
entrance_fee = float(input())
chair_price = float(input())
umbrella_price = float(input())
chair_number = ceil(0.75 * number_of_people)
umbrella_number = ceil(number_of_people / 2)
total_price = umbrella_price * umbrella_number + chair_number * chair_price + number_of_people * entrance_fee
print(f'{total_price:.2f} lv.')