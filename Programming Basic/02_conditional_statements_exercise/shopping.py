budjet = float(input())
N = int(input())
M = int(input())
P = int(input())

price_N = N * 250
price_M = price_N * 0.35 * M
price_P = price_N * 0.1 * P
price = price_N + price_M + price_P

if N > M:
    price -= price * 0.15

diff = abs(budjet - price)
if budjet >= price:
    print(f"You have {diff:.2f} leva left!")
else:
    print(f"Not enough money! You need {diff:.2f} leva more!")