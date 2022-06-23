def calculator(command, number):
    result = 0
    if command == 'coffee':
        result = 1.5 * number
    elif command == 'water':
        result = number
    elif command == 'coke':
        result = number * 1.4
    elif command == 'snacks':
        result = number * 2.00
    return f'{result:.2f}'


drink = input()
quantity = int(input())
print(calculator(drink, quantity))

