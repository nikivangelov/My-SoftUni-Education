tourist_number = int(input())
season = input()

price = 0
if tourist_number <= 5:
    if season == 'spring':
        price = 50 * tourist_number
    elif season == 'summer':
        price = 48.5 * 0.85 * tourist_number
    elif season == 'autumn':
        price = 60 * tourist_number
    elif season == 'winter':
        price = 1.08 * 86 * tourist_number
else:
    if season == 'spring':
        price = 48 * tourist_number
    elif season == 'summer':
        price = 45 * 0.85 * tourist_number
    elif season == 'autumn':
        price = 49.5 * tourist_number
    elif season == 'winter':
        price = 1.08 * 85 * tourist_number

print(f'{price:.2f} leva.')