number_of_orders = int(input())
total_price = 0
for _ in range(number_of_orders):
    price_per_cpasule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if 0.01 <= price_per_cpasule <= 100 and 1 <= days <= 31 and 1 <= capsules_per_day <= 2000:
        current_price = price_per_cpasule * days * capsules_per_day
        print(f"The price for the coffee is: ${current_price:.2f}")
        total_price += current_price
    else:
        continue

print(f'Total: ${total_price:.2f}')
