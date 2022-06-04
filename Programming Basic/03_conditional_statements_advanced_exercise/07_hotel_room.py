month = input()
nights = int(input())
price_a = 0
price_s = 0
if month == 'May' or month == 'October':
    price_s = nights * 50
    price_a = nights * 65
    if 7 < nights <= 14:
        price_s -= price_s * 0.05
    elif nights > 14:
        price_s -= price_s * 0.3
        price_a -= price_a * 0.1
elif month == 'June' or month == 'September':
    price_s = nights * 75.2
    price_a = nights * 68.7
    if nights > 14:
            price_s -= price_s * 0.2
            price_a -= price_a * 0.1
elif month == 'July' or month == 'August':
    price_s = nights * 76
    price_a = nights * 77
    if nights > 14:
        price_a -= price_a * 0.1

print(f'Apartment: {price_a:.2f} lv.')
print(f'Studio: {price_s:.2f} lv.')

