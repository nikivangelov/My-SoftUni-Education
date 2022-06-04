chicken_menu = int(input())
fish_menu = int(input())
vegy_menu = int(input())
total_chicken = chicken_menu * 10.35
total_fish = fish_menu * 12.40
total_vegy = vegy_menu * 8.15
main_menu = total_vegy + total_fish + total_chicken
desert = main_menu * 0.2
total_price = main_menu + desert + 2.50
print(total_price)