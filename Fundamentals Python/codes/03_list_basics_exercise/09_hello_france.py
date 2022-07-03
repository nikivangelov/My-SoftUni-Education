collection_of_items = input().split('|')
starting_budjet = int(input())
budjet = starting_budjet
sales = 0
profit = 0
price_list = []

for item in range(len(collection_of_items)):
    current_item = collection_of_items[item].split('->')
    item_name = current_item[0]
    item_price = float(current_item[1])
    new_price = 0
    if item_name == 'Clothes':
        if item_price <= 50 and item_price <= budjet:
            budjet -= item_price
            new_price = 1.4 * item_price
            price_list.append(f"{new_price:.2f}")
            sales += new_price
            profit += new_price - item_price
        else:
            continue
    if item_name == 'Shoes':
        if item_price <= 35 and item_price <= budjet:
            new_price = 1.4 * item_price
            budjet -= item_price
            sales += new_price
            price_list.append(f"{new_price:.2f}")
            profit += new_price - item_price
        else:
            continue
    if item_name == 'Accessories' and item_price <= budjet:
        if item_price <= 20.5:
            new_price = 1.4 * item_price
            budjet -= item_price
            sales += new_price
            price_list.append(f"{new_price:.2f}")
            profit += new_price - item_price
        else:
            continue

    if budjet <= 0:
        break


print(*price_list, sep=" ")
print(f"Profit: {profit:.2f}")
if budjet + sales >= 150:
    print('Hello, France!')
else:
    print('Not enough money.')


