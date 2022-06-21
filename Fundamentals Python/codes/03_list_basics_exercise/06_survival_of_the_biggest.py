list_of_integers = input().split(" ")
removal_count = int(input())
list_of_integers_as_digits = []
for integer in range(len(list_of_integers)):
    list_of_integers_as_digits.append(int(list_of_integers[integer]))

list_of_integers_as_digits.sort(reverse = True)
removed_integers = []
for current_removal in range(removal_count):
    removed_integers.append(list_of_integers_as_digits.pop(-1))

for index in range(len(removed_integers)):
    list_of_integers.remove(str(removed_integers[index]))
for separated_integer in range(len(list_of_integers)):
    if separated_integer == len(list_of_integers) - 1:
        print(list_of_integers[separated_integer], end="")
        break
    print(list_of_integers[separated_integer], end= ", ")
# final_list = []
# for final_digit in range(len(list_of_integers)):
#     final_list.append(int(list_of_integers[final_digit]))
#
# print(final_list)