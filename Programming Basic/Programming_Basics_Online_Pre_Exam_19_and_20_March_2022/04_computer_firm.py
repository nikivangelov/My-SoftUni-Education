n = int(input())
rating = 0
potential_sales = 0
sales = 0
rating_sum = 0

for i in range(1, n+1):
    number = int(input())
    rating = number % 10
    potential_sales = (number - rating) / 10
    rating_sum += rating
    if rating == 2:
        sales += 0 * potential_sales
    elif rating == 3:
        sales += 0.5 * potential_sales
    elif rating == 4:
        sales += 0.7 * potential_sales
    elif rating == 5:
        sales += 0.85 * potential_sales
    elif rating == 6:
        sales += 1 * potential_sales

print(f'{sales:.2f}')
print(f'{rating_sum / n :.2f}')