import re

total_price = 0
pattern = r">>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)"
item_list = []
while True:
    command = input()
    if command == 'Purchase':
        break

    match = re.search(pattern, command)
    if match:
        item = match.group(1)
        item_list.append(item)
        price = match.group(2)
        quantity = match.group(3)
        total_price += float(price) * int(quantity)

print(f'Bought furniture:')
for i in item_list:
    print(i)
print(f'Total money spend: {total_price:.2f}')