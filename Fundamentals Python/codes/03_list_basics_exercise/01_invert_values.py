numbers = input().split(' ')
opposite_string = []
for element in range(len(numbers)):
    new_element = int(numbers[element]) * (-1)
    opposite_string.append(new_element)
print(opposite_string)