version_list = input().split('.')
number = int(version_list[0] + version_list[1] + version_list[2])
next_number = number + 1
version_list = []
new_number = 0
for i in range(3):
    new_number = next_number % 10
    next_number = next_number // 10
    version_list.insert(0, str(new_number))
version = '.'.join(version_list)
print(version)

