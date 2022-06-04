n = int(input())
odd_condition = False
for i in range(1, n+1):
    num = int(input())
    if num % 2 != 0:
        odd_condition = True
        break
    else:
        continue

if not odd_condition:
    print(f'All numbers are even.')
else:
    print(f'{num} is odd!')
