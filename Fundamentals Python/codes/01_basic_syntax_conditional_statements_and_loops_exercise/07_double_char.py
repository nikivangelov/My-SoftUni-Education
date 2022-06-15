while True:
    string = input()
    if string == 'End':
        break
    elif string == 'SoftUni':
        continue
    else:
        new_string = ''
        for char in range(len(string)):
            new_string += string[char] * 2
        print(new_string)

