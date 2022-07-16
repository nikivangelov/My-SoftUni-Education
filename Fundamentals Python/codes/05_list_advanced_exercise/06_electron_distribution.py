electron_number = int(input())
shell = 0
filled_electrons = []
left_electrons = electron_number
while left_electrons > 0:
    shell += 1
    shell_capacity = 2 * shell ** 2
    if left_electrons < shell_capacity:
        filled_electrons.append(left_electrons)
        break
    filled_electrons.append(shell_capacity)
    left_electrons -= shell_capacity
print(filled_electrons)