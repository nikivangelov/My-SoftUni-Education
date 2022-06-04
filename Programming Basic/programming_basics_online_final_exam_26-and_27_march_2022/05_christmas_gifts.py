
adults_number = 0
kids_number = 0
toy_count = 0
sweaters_count = 0
while True:
    member_age = input()
    if member_age == 'Christmas':
        break

    if int(member_age) <= 16:
        kids_number += 1
    else:
        adults_number += 1

toys_price = kids_number * 5
sweaters_price = adults_number * 15
print(f'Number of adults: {adults_number}')
print(f'Number of kids: {kids_number}')
print(f'Money for toys: {toys_price}')
print(f'Money for sweaters: {sweaters_price}')