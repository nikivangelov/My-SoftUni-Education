def calculator(command: str, a: int, b: int):
    result = 0
    if command == 'multiply':
        result = int(a * b)
    elif command == 'divide':
        result = int(a / b)
    elif command == 'add':
        result = a + b
    elif command == 'subtract':
        result = a - b
    return result


operator = input()
first_num = int(input())
second_num = int(input())
print(calculator(operator, first_num, second_num))

