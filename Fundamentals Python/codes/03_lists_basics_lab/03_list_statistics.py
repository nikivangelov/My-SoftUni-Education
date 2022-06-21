n = int(input())
list_positives = []
list_negatives = []
count_positives = 0
sum_of_negatives = 0
for _ in range(n):
    number = int(input())
    if number >= 0:
        list_positives.append(number)
        count_positives += 1
    else:
        list_negatives.append(number)
        sum_of_negatives += number

print(list_positives)
print(list_negatives)
print(f"Count of positives: {count_positives}")
print(f"Sum of negatives: {sum_of_negatives}")


