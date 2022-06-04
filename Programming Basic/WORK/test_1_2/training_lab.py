w = float(input('Въведете дължина между 3 и 100 '))
h = float(input('Въведете широчина в интервал между 3 и дължината '))
used_width = h * 100 - 100
desks_in_row = used_width // 70
desks_in_column = w * 100 // 120
total_desks = desks_in_row * desks_in_column - 3
print(total_desks)
