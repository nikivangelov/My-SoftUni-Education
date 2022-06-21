n = int(input())
numbers = []
filtered_numbers = []
COMMAND_EVEN = 'even'
COMMAND_ODD = 'odd'
COMMAND_NEGATIVE = 'negative'
COMMAND_POSITIVE = 'positive'

for _ in range(n):
    number = int(input())
    numbers.append(number)

command = input()

for num in numbers:
    filterd_command = (
        (command == COMMAND_EVEN and num % 2 == 0) or
        (command == COMMAND_ODD and num % 2 != 0) or
        (command == COMMAND_NEGATIVE and num < 0) or
        (command == COMMAND_POSITIVE and num >= 0)
    )
    if filterd_command:
        filtered_numbers.append(num)

print(filtered_numbers)
