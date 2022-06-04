import random
from string import digits, punctuation, ascii_lowercase, ascii_uppercase

all_combination_from_digits_letters_symbols = digits + punctuation + ascii_lowercase + ascii_uppercase

password_lenght = int(input('Enter the password lenght: '))

password = ''.join(random.sample(all_combination_from_digits_letters_symbols, password_lenght))

print(f'This is your current password: {password}')