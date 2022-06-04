month = input()
hours = int(input())
members_number = int(input())
day_time = input()

price = 0
if month == 'march' or month == 'april' or month == 'may':
    if day_time == 'night':
        price += 8.4
    elif day_time == 'day':
        price += 10.5

elif month == 'june' or month == 'july' or month == 'august':
    if day_time == 'night':
        price += 10.2
    elif day_time == 'day':
        price += 12.6

if members_number >= 4:
    price -= price * 0.1

if hours >= 5:
    price -= price * 0.5

total_sum = price * members_number * hours
print(f'Price per person for one hour: {price:.2f}')
print(f'Total cost of the visit: {total_sum:.2f}')