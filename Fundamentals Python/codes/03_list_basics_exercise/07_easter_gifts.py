names_of_the_gifts = input().split(' ')

while True:
    command = input().split(' ')
    new_list = []
    if ['No', 'Money'] == command:
        break

    elif 'OutOfStock' in command:
        for outofstock_gift in names_of_the_gifts:
            out_of_stock = outofstock_gift.replace(command[1], 'None')
            new_list.append(out_of_stock)

    elif 'Required' in command:
        if int(command[2]) >= len(command):
            continue

        names_of_the_gifts[int(command[2])] = command[1]
        new_list = names_of_the_gifts

    elif 'JustInCase' in command:
        names_of_the_gifts[-1] = command[1]
        new_list = names_of_the_gifts
    else:
        new_list = names_of_the_gifts

    names_of_the_gifts = new_list

for i in range(len(names_of_the_gifts)):
    if 'None' in names_of_the_gifts:
        names_of_the_gifts.remove('None')

print(" ".join(names_of_the_gifts))
