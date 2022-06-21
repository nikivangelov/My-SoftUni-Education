begin_number = int(input())
last_number = int(input())
magic_number = int(input())

combination_count = 0
is_found = False
for aber in range(begin_number, last_number + 1):
    for bber in range(begin_number, last_number + 1):
        combination_count += 1
        if magic_number == aber + bber:
            print(f'Combination N:{combination_count} ({aber} + {bber} = {magic_number})')
            is_found = True
            break

    if is_found:
        break

if not is_found:
    print(f'{combination_count} combinations - neither equals {magic_number}')

