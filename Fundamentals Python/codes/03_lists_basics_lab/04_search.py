n = int(input())
word = input()
list_of_strings = []
list_word_included = []
for _ in range(n):
    opposite_string = input()
    list_of_strings.append(opposite_string)
    if word in opposite_string:
        list_word_included.append(opposite_string)

print(list_of_strings)
print(list_word_included)