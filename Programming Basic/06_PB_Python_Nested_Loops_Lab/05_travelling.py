while True:
    destination = input()
    if destination == 'End':
        break
    budjet = float(input())
    total_savings = 0
    while total_savings < budjet:
        savings = input()
        total_savings += float(savings)

    print(f'Going to {destination}!')
