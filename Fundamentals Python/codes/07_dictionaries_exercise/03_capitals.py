countries = input().split(', ')
cities = input().split(', ')
zipped = zip(countries, cities)
country_capital = {key: value for (key, value) in list(zipped)}
for key, value in country_capital.items():
    print(f"{key} -> {value}")
