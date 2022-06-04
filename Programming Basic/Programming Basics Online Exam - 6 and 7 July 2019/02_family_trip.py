budjet = float(input())
number_of_nights = int(input())
price_per_night = float(input())
percentage_additional_expenses = int(input()) / 100
if number_of_nights > 7:
    price_per_night = price_per_night - price_per_night * 0.05

total_price = price_per_night * number_of_nights + budjet * percentage_additional_expenses
diff = abs(total_price - budjet)
if budjet >= total_price:
    print(f'Ivanovi will be left with {diff:.2f} leva after vacation.')
else:
    print(f'{diff:.2f} leva needed.')

