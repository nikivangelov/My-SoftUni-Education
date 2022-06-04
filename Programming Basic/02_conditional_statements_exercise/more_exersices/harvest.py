from math import floor, ceil

x = int(input())
y = float(input())
z = int(input())
workers = int(input())
total_harvest = x * y
grapes_harvest = 0.4 * total_harvest
total_liters = grapes_harvest / 2.5
diff = abs(total_liters - z)
if total_liters < z:
    diff = floor(diff)
    print(f'It will be a tough winter! More {diff:.0f} liters wine needed.')
else:
    print(f"Good harvest this year! Total wine: {total_liters:.0f} liters.")
    wine_per_worker = ceil(diff / workers)
    print(f'{diff:.0f} liters left -> {wine_per_worker:.0f} liters per person.')