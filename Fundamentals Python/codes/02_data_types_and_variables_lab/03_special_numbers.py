n = int(input())


for i in range(100, n+1):
    sum = 0
    digits = i
    special = False
    while digits > 0:
        sum += digits % 10
        digits = int(digits/10)
    if sum == 5 or sum == 7 or sum == 11:
        special = True

    print(f'{i} -> {special}')