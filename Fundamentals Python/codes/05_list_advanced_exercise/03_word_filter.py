text_list = input().split(' ')
new_list = [x for x in text_list if len(x) % 2 == 0]
print(*new_list, sep='\n')