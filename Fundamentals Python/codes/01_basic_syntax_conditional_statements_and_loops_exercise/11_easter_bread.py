budjet = float(input())
flour_price = float(input())
egg_price = 0.75 * flour_price
milk_price = 1.25 * flour_price / 4
price_per_loaf = flour_price + egg_price + milk_price
loaves_quantity = int(budjet // price_per_loaf)
money_left = budjet - loaves_quantity * price_per_loaf
egg_count = 0
for i in range(1, loaves_quantity + 1):
    egg_count += 3
    if i % 3 == 0:
        egg_count -= i - 2

print(f"You made {loaves_quantity} loaves of Easter bread! Now you have {egg_count} eggs and {money_left:.2f}BGN left.")
