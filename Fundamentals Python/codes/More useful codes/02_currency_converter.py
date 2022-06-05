from forex_python.convereter import CurrencyRates

amount = int(input())
c = CurrencyRates()
current_rate = c.get_rate('GBP', 'USD')
result = current_rate * amount
print(f'Your sum in dollars is : {result:.3f}')

