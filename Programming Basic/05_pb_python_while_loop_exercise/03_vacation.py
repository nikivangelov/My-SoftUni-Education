money_for_vacation = float(input())
starting_budjet = float(input())
spend_days_counter = 0
days_counter = 0
current_budjet = starting_budjet
he_failed = False

while money_for_vacation > current_budjet:
    transaction = input()
    sum_of_transaction = float(input())
    days_counter += 1
    if transaction == 'spend':
        spend_days_counter += 1
        current_budjet -= sum_of_transaction
        if current_budjet < 0:
            current_budjet = 0
    elif transaction == 'save':
        spend_days_counter = 0
        current_budjet += sum_of_transaction

    if spend_days_counter == 5:
        he_failed = True
        break

if he_failed:
    print("You can't save the money.")
    print(f'{days_counter}')
else:
    print(f'You saved the money for {days_counter} days.')
