resource_dict = {}
while True:
    current_resource = input()
    if current_resource == 'stop':
        break
    quantity = int(input())
    if current_resource not in resource_dict.keys():
        resource_dict[current_resource] = 0
    resource_dict[current_resource] += quantity

for key, value in resource_dict.items():
    print(f"{key} -> {value}")