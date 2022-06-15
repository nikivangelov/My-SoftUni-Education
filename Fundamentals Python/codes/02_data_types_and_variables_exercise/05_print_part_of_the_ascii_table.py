first_char = int(input())
last_char = int(input())
sum_of_chars = ''
for i in range(first_char, last_char + 1):
    symbol = chr(i) + ' '
    if i == last_char:
        symbol = chr(i)

    sum_of_chars += symbol

print(sum_of_chars)