from math import ceil

average_speed = float(input())
fuel_consumption = float(input())
total_direction = 384400 * 2
time_flying = total_direction / average_speed
total_time = ceil(time_flying + 3)
total_fuel = int(total_direction * fuel_consumption / 100)
print(total_time)
print(total_fuel)