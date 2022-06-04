N1 = int(input())
N2 = int(input())
symbol = input()
result = 0
even_odd = ''
if symbol == '+':
    result = N1 + N2
    if result % 2 == 0:
        even_odd = 'even'
        print(f'{N1} {symbol} {N2} = {result} - {even_odd}')
    else:
        even_odd = 'odd'
        print(f'{N1} {symbol} {N2} = {result} - {even_odd}')
elif symbol == '-':
    result = N1 - N2
    if result % 2 == 0:
        even_odd = 'even'
        print(f'{N1} {symbol} {N2} = {result} - {even_odd}')
    else:
        even_odd = 'odd'
        print(f'{N1} {symbol} {N2} = {result} - {even_odd}')
elif symbol == '*':
    result = N1 * N2
    if result % 2 == 0:
        even_odd = 'even'
        print(f'{N1} {symbol} {N2} = {result} - {even_odd}')
    else:
        even_odd = 'odd'
        print(f'{N1} {symbol} {N2} = {result} - {even_odd}')

elif symbol == '/':
    if N2 == 0:
        print(f'Cannot divide {N1} by zero')
    else:
        result = N1 / N2
        print(f'{N1} / {N2} = {result:.2f}')
elif symbol == '%':
    if N2 == 0:
        print(f'Cannot divide {N1} by zero')
    else:
        result = N1 % N2
        print(f'{N1} % {N2} = {result}')
