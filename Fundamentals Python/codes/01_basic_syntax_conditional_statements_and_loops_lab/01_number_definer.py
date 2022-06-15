number = float(input())
positive_or_negative = ''

if number == 0:
    print(f'zero')

elif number > 0:
    positive_or_negative = 'positive'
    if 0 < abs(number) < 1:
        print(f'small {positive_or_negative}')
    elif 1 <= abs(number) < 1000000:
        print(positive_or_negative)
    else:
        print(f'large {positive_or_negative}')
else:
    positive_or_negative = 'negative'

    if 0 < abs(number) < 1:
        print(f'small {positive_or_negative}')
    elif 1 <= abs(number) < 1000000:
        print(positive_or_negative)
    else:
        print(f'large {positive_or_negative}')

