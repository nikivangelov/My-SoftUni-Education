quantity_of_decoration = int(input())
remaining_days = int(input())
total_price = 0
total_spirit = 0
for day in range(1, remaining_days + 1):
    if day % 11 == 0:
        quantity_of_decoration += 2

    if day % 2 == 0:
        total_price += 2 * quantity_of_decoration
        total_spirit += 5

    if day % 3 == 0:
        total_price += 8 * quantity_of_decoration
        total_spirit += 13

    if day % 5 == 0:
        total_price += 15 * quantity_of_decoration
        total_spirit += 17
        if day % 3 == 0:
            total_spirit += 30

    if day % 10 == 0:
        total_spirit -= 20
        total_price += 23

if remaining_days % 10 == 0:
    total_spirit -= 30

print(f"Total cost: {total_price}")
print(f"Total spirit: {total_spirit}")

