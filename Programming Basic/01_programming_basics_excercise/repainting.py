nylon = int(input())
paint = int(input())
thiner = int(input())
working_hours = int(input())
total_paint = (paint + paint * 0.1) * 14.50
total_nylon = (nylon + 2) * 1.50
total_thiner = thiner * 5
materials = total_thiner + total_nylon + total_paint + 0.4
workers = materials * 0.3 * working_hours
total_price = materials + workers
print(total_price)
