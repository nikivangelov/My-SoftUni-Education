budjet = float(input())
season = input()
place_to_stay = ''
accomodation = ''
costs = 0
if season == 'summer':
    if budjet <= 100:
        place_to_stay = 'Bulgaria'
        accomodation = 'Camp'
        costs = 0.3 * budjet
    elif 100 < budjet <= 1000:
        place_to_stay = 'Balkans'
        accomodation = 'Camp'
        costs = 0.4 * budjet
    else:
        place_to_stay = 'Europe'
        accomodation = 'Hotel'
        costs = 0.9 * budjet
elif season == 'winter':
    if budjet <= 100:
        place_to_stay = 'Bulgaria'
        accomodation = 'Hotel'
        costs = 0.7 * budjet
    elif 100 < budjet <= 1000:
        place_to_stay = 'Balkans'
        accomodation = 'Hotel'
        costs = 0.8 * budjet
    else:
        place_to_stay = 'Europe'
        accomodation = 'Hotel'
        costs = 0.9 * budjet

print(f'Somewhere in {place_to_stay}')
print(f'{accomodation} - {costs:.2f}')