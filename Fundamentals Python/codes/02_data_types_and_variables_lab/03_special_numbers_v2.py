n = input()
current_num = 0
current_digit = ''
sum = 0
special_number = False
for i in range(1, int(n) + 1):
    for j in str(i):
        sum += int(j)
    if sum == 5 or sum == 7 or sum == 11:
        special_number = True

    print(f'{i} -> {special_number}')
    sum = 0
    special_number = False


