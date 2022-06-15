n = int(input())
for _ in range(1,n+1):
    number = int(input())
    if number == 88:
        print('Hello')
    elif number == 86:
        print('How are you?')
    else:
        if number < 88:
            print('GREAT!')
        else:
            print('Bye.')