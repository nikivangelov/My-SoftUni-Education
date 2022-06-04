target_profit = int(input())

profit = 0
condition = False
while True:
    cocktail_name = input()
    if cocktail_name == 'Party!':
        break

    number_of_cocktails = int(input())
    order_price = len(cocktail_name) * int(number_of_cocktails)
    if order_price % 2 == 1:
        order_price *= 0.75

    profit += order_price
    if profit >= target_profit:
        condition = True
        break

diff = abs(target_profit - profit)
if condition:
    print('Target acquired.')
else:
    print(f'We need {diff:.2f} leva more.')

print(f'Club income - {profit:.2f} leva.')