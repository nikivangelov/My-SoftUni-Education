group_size = int(input())
days_of_adventure = int(input())
current_group_size = group_size
total_profit = 0
companion_profit = 0
for current_day in range(1, days_of_adventure + 1):
    profit_per_companion = 0
    if current_day % 10 == 0:
        current_group_size -= 2

    if current_day % 15 == 0:
        current_group_size += 5
        profit_per_companion -= 2

    if current_day % 3 == 0:
        profit_per_companion -= 3

    if current_day % 5 == 0:
        profit_per_companion += 20

    current_day_profit = 50 - 2 * current_group_size + profit_per_companion * current_group_size
    total_profit += current_day_profit

final_profit_per_companion = total_profit // current_group_size
print(f"{current_group_size} companions received {final_profit_per_companion} coins each.")

