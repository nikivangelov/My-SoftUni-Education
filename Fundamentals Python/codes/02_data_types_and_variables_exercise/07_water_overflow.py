number_of_pourings = int(input())
total_liters = 0
for i in range(1, number_of_pourings + 1):
    current_litters = int(input())
    if total_liters + current_litters > 255:
        print("Insufficient capacity!")
        continue
    else:
        total_liters += current_litters

print(total_liters)