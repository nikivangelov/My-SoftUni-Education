screening = input()
r = int(input())
c = int(input())
total_seats = r * c
price = 0
if screening == 'Premiere':
    price = 12 * total_seats
elif screening == 'Normal':
    price = 7.5 * total_seats
elif screening == 'Discount':
    price = 5 * total_seats

print(f'{price:.2f} leva')