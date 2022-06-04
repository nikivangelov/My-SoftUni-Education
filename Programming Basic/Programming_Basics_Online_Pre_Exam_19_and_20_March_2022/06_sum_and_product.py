#a се мени от 1 до 9
#b се мени от 9 до а
#c се мени от 0 до 9
#d се мени от 9 до c
n = int(input())
is_found_1 = False
is_found_2 = False
for a in range(1, 10):
    for b in range(9, a, -1):
        for c in range(0, 10):
            for d in range(9, c, -1):
                if (a + b + c + d) == (a * b * c * d) and n % 10 == 5:
                    print(f'{a}{b}{c}{d}')
                    is_found_1 = True
                    break
                elif (a * b * c * d) // (a + b + c + d) == 3 and n % 3 == 0:
                    print(f'{d}{c}{b}{a}')
                    is_found_2 = True
                    break

            if is_found_1 or is_found_2:
                    break
        if is_found_1 or is_found_2:
            break
    if is_found_1 or is_found_2:
        break

if not is_found_1 and not is_found_2:
    print('Nothing found')

