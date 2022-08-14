import re

regex = r'\d+'
text = input()
text_list = []
while len(text) != 0:
    digit_reg = re.findall(regex, text)
    if digit_reg:
        print(' '.join(digit_reg), end=' ')

    text = input()