vacantion_price = float(input())
count_puzzels = int(input())
count_dolls = int(input())
count_bears = int(input())
count_minions = int(input())
count_busses = int(input())
price = count_puzzels * 2.6 + count_dolls * 3 + count_bears * 4.1 + count_minions * 8.2 + count_busses * 2
total_count = count_puzzels + count_dolls + count_bears + count_minions + count_busses
if total_count >= 50:
    price -= price * 0.25

rent = price * 0.1
result = price - rent
diff = abs(result - vacantion_price)
if result >= vacantion_price:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")