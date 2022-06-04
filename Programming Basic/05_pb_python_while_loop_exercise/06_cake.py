widht_cake = int(input())
lenght_cake = int(input())
cake_pieces = widht_cake * lenght_cake
taken_pieces = 0
while True:
    guests_pieces = input()
    if guests_pieces == 'STOP':
        break

    taken_pieces += int(guests_pieces)
    if taken_pieces >= cake_pieces:
        break

diff = abs(taken_pieces - cake_pieces)
if taken_pieces <= cake_pieces:
    print(f'{diff} pieces are left.')
else:
    print(f'No more cake left! You need {diff} pieces more.')
