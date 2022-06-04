budjet = float(input())
extra = int(input())
price_clothing_per_extra = float(input())
decor = budjet * 0.1
if extra > 150:
    price_clothing_per_extra -= price_clothing_per_extra * 0.1

total_clothing = extra * price_clothing_per_extra
total_expenses = total_clothing + decor
diff = abs(budjet - total_expenses)
if total_expenses > budjet:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")