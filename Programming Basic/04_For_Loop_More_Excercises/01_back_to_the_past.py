legacy = float(input())
year_to_live = int(input())
expenses = 0
for i in range(1800, year_to_live + 1):
    if (i - 1800) % 2 == 0:
        expenses += 12000
    elif (i - 1800) % 2 == 1:
        expenses += 12000 + 50 * (18 + i - 1800)

diff = abs(legacy - expenses)
if legacy >= expenses:
    print(f'Yes! He will live a carefree life and will have {diff:.2f} dollars left.')
else:
    print(f'He will need {diff:.2f} dollars to survive.')