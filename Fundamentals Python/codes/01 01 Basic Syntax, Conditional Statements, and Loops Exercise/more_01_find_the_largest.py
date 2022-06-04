number = input()
numberlist = []
current_digit = ''
for digit in range(len(number)):
    numberlist.extend(number[digit])
    numberlist.sort(reverse=True)
print(''.join(numberlist))





