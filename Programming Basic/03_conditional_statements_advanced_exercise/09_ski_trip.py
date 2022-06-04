period = int(input())
accomodation = input()
rate = input()
stay = period - 1
price = 0
if accomodation == 'room for one person':
    price = stay * 18

elif accomodation == 'apartment':
    price = stay * 25
    if period < 10:
        price -= price * 0.3
    elif 10 <= period <= 15:
        price -= price * 0.35
    elif period > 15:
        price -= price * 0.5

elif accomodation == 'president apartment':
    price = stay * 35
    if period < 10:
        price -= price * 0.1
    elif 10 <= period <= 15:
        price -= price * 0.15
    elif period > 15:
        price -= price * 0.2


if rate == 'positive':
    price += price * 0.25
elif rate == 'negative':
    price -= price * 0.1

print(f'{price:.2f}')


