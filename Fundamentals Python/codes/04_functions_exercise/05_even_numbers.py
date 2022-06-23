def even_numbers(num):
    if num % 2 == 0:
        return True
    else:
        return False


number_list = [int(s) for s in input().split(' ')]
result = filter(even_numbers, number_list)
final = list(result)
print(final)
