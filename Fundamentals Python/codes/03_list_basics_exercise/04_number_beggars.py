gained_coins = input().split(', ')
beggars = int(input())
earnings_list = []
for current_beggar in range(beggars):
    current_beggar_earnings = 0
    for current_earnings in range(current_beggar, len(gained_coins), beggars):
        current_beggar_earnings += int(gained_coins[current_earnings])
    earnings_list.append(current_beggar_earnings)
print(earnings_list)