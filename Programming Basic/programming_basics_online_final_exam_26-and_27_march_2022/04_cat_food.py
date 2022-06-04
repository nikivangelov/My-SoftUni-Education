cats_number = int(input())

small_cats_count = 0
medium_cats_count = 0
big_cats_count = 0
total_food = 0
for i in range(1, cats_number + 1):
    food_in_grams = float(input())
    total_food += food_in_grams
    if 100 <= food_in_grams < 200:
        small_cats_count += 1
    elif 200 <= food_in_grams < 300:
        medium_cats_count += 1
    elif 300 <= food_in_grams < 400:
        big_cats_count += 1

food_price = (total_food / 1000) * 12.45
print(f'Group 1: {small_cats_count} cats.')
print(f'Group 2: {medium_cats_count} cats.')
print(f'Group 3: {big_cats_count} cats.')
print(f'Price for food per day: {food_price:.2f} lv.')