number_of_letters = int(input())
triple = ''
for first_letter in range(ord('a'), ord('a') + number_of_letters):
    triple = chr(first_letter)
    for second_letter in range(ord('a'), ord('a') + number_of_letters):
        triple = chr(first_letter) + chr(second_letter)
        for third_letter in range(ord('a'), ord('a') + number_of_letters):
            result = chr(first_letter) + chr(second_letter) + chr(third_letter)
            print(result)
