first_string = input()
second_string = input()
new_string = ''
for char in range(len(first_string)):
    if second_string[char] != first_string[char]:
        new_string = first_string[char+1:]
        print(f'{second_string[:char+1]}{new_string}')
    else:
        continue
