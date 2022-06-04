drink_name = input()
sugar = input()
number_of_drinks = int(input())
price = 0

if drink_name == 'Espresso':
    if sugar == 'Without':
        price = 0.9 * 0.65
    elif sugar == 'Normal':
        price = 1
    elif sugar == 'Extra':
        price = 1.2

if drink_name == 'Cappuccino':
    if sugar == 'Without':
        price = 1 * 0.65
    elif sugar == 'Normal':
        price = 1.2
    elif sugar == 'Extra':
        price = 1.6

if drink_name == 'Tea':
    if sugar == 'Without':
        price = 0.5 * 0.65
    elif sugar == 'Normal':
        price = 0.6
    elif sugar == 'Extra':
        price = 0.7

if number_of_drinks > 5 and drink_name == 'Espresso':
    price *= 0.75

total_price = number_of_drinks * price
if total_price > 15:
    total_price *= 0.8

print(f'You bought {number_of_drinks} cups of {drink_name} for {total_price:.2f} lv.')