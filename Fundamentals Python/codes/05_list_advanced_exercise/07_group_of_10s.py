number_sequence = [int(x) for x in input().split(', ')]
max_num = max(number_sequence)
max_group = (max_num // 10 + 1) * 10
for group in range(10, max_group + 1, 10):
    group_list = list(filter(lambda y: group - 10 < y <= group, number_sequence))
    if len(number_sequence) == 0:
        break
    print(f"Group of {group}'s: {group_list}")
    for num in group_list:
        number_sequence.remove(num)
