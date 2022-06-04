age = int(input())
price_washing_machine = float(input())
price_per_toy = int(input())
toys_count = 0
money = 0
for i in range(1, age+1, 2):
    toys_count += 1

for i in range(2, age+1, 2):
    money += i * 5 -1

total_money = toys_count * price_per_toy + money
diff = abs(total_money - price_washing_machine)

if total_money >= price_washing_machine:
    print(f'Yes! {diff:.2f}')
else:
    print(f'No! {diff:.2f}')