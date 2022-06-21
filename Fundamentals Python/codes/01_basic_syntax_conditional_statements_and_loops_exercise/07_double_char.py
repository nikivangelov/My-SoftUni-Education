while True:
    string = input()
    if string == 'End':
        break
    elif string == 'SoftUni':
        continue
    else:
        opposite_string = ''
        for char in range(len(string)):
            opposite_string += string[char] * 2
        print(opposite_string)

