income = input()
sum = 0
while income != 'NoMoreMoney':
    amount = float(income)
    if amount < 0:
        print('Invalid operation!')
        break

    else:
        print(f'Increase: {amount:.2f}')
        sum += amount
        income = input()


print(f'Total: {sum:.2f}')

