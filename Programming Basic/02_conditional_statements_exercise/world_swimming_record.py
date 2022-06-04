from math import floor

record = float(input())
distance = float(input())
time_per_meter = float(input())
clear_time = distance * time_per_meter
resistance_in_distance = floor(distance / 15)
resistant_time = resistance_in_distance * 12.5
ivan_time = clear_time + resistant_time
if ivan_time < record:
    print(f" Yes, he succeeded! The new world record is {ivan_time:.2f} seconds.")
else:
    diff = abs(record - ivan_time)
    print(f"No, he failed! He was {diff:.2f} seconds slower.")
