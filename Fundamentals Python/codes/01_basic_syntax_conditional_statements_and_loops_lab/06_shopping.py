budjet = int(input())
bill = 0
product = input()
enough_money = True
while product != 'End':
    bill += int(product)
    if bill > budjet:
        print(f'You went in overdraft!')
        enough_money = False
        break
    else:
        product = input()

if enough_money:
    print(f'You bought everything needed.')
