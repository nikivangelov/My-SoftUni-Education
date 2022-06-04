product = input()
city = input()
quantity = float(input())
price = 0
if city == 'Sofia':
    if product == 'coffee':
        price = 0.5 * quantity
        print(price)
    elif product == 'water':
        price = 0.8 * quantity
        print(price)
    elif product == 'beer':
        price = 1.2 * quantity
        print(price)
    elif product == 'sweets':
        price = 1.45 * quantity
        print(price)
    elif product == 'peanuts':
        price = 1.6 * quantity
        print(price)
elif city == 'Plovdiv':
    if product == 'coffee':
        price = 0.4 * quantity
        print(price)
    elif product == 'water':
        price = 0.7 * quantity
        print(price)
    elif product == 'beer':
        price = 1.15 * quantity
        print(price)
    elif product == 'sweets':
        price = 1.30 * quantity
        print(price)
    elif product == 'peanuts':
        price = 1.5 * quantity
        print(price)
elif city == 'Varna':
    if product == 'coffee':
        price = 0.45 * quantity
        print(price)
    elif product == 'water':
        price = 0.7 * quantity
        print(price)
    elif product == 'beer':
        price = 1.1 * quantity
        print(price)
    elif product == 'sweets':
        price = 1.35 * quantity
        print(price)
    elif product == 'peanuts':
        price = 1.55 * quantity
        print(price)
