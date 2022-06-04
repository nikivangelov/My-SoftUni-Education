turn = int(input())
result = 0
n1 = 0
n2 = 0
n3 = 0
n4 = 0
n5 = 0
n6 = 0
invalid_num = 0
for _ in range(1, turn + 1):
    number = int(input())
    if 0 <= number <= 9:
        result += 0.2 * number
        n1 += 1
    elif 10 <= number <= 19:
        result += 0.3 * number
        n2 += 1
    elif 20 <= number <= 29:
        result += 0.4 * number
        n3 += 1
    elif 30 <= number <= 39:
        result += 50
        n4 += 1
    elif 40 <= number <= 50:
        result += 100
        n5 += 1
    else:
        result = result / 2
        n6 += 1

print(f'{result:.2f}')
print(f'From 0 to 9: {n1 / turn * 100:.2f}%')
print(f'From 10 to 19: {n2 / turn * 100:.2f}%')
print(f'From 20 to 29: {n3 / turn * 100:.2f}%')
print(f'From 30 to 39: {n4 / turn * 100:.2f}%')
print(f'From 40 to 50: {n5 / turn * 100:.2f}%')
print(f'Invalid numbers: {n6 / turn * 100:.2f}%')