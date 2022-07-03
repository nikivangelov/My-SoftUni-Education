fire_list = input().split('#')
water_amount = int(input())
total_effort = 0
total_fire = 0
cell_list = []
for current_cell in range(len(fire_list)):
    level_of_fire_list = fire_list[current_cell].split(' = ')
    fire_level = level_of_fire_list[0]
    cell_value = int(level_of_fire_list[1])
    if water_amount >= cell_value:
        if fire_level == 'High':
            if 81 <= cell_value <= 125:
                cell_list.append(f" - {cell_value}")
                total_effort += 0.25 * cell_value
                water_amount -= cell_value
                total_fire += cell_value
            else:
                continue
        if fire_level == 'Medium':
            if 51 <= cell_value <= 80:
                cell_list.append(f" - {cell_value}")
                total_effort += 0.25 * cell_value
                water_amount -= cell_value
                total_fire += cell_value
            else:
                continue
        if fire_level == 'Low':
            if 1 <= cell_value <= 50:
                cell_list.append(f" - {cell_value}")
                total_effort += 0.25 * cell_value
                water_amount -= cell_value
                total_fire += cell_value
            else:
                continue

    else:
        continue

print('Cells:', *cell_list, sep="\n")
print(f'Effort: {total_effort:.2f}')
print(f'Total Fire: {total_fire}')
