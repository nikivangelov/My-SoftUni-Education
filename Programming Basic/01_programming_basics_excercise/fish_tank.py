lenght = int(input())
widht = int(input())
height = int(input())
percentage = float(input())

volume = lenght * widht * height
volume_in_liters = volume / 1000
other_volume = volume_in_liters * (percentage/100)
water = volume_in_liters - other_volume
print(water)