city = input()
package = input()
vip_card = input()
nights = int(input())

days_negative_condition = True
invalid_input_condition = False
price = 0

if nights >= 1:
    days_negative_condition = False
    if nights > 7:
        nights -= 1

    if city == 'Bansko' or city == 'Borovets':
        if package == 'noEquipment':
            if vip_card == 'yes':
                price = 80 * 0.95
            elif vip_card == 'no':
                price = 80

        elif package == 'withEquipment':
            if vip_card == 'yes':
                price = 100 * 0.9
            elif vip_card == 'no':
                price = 100
        else:
            invalid_input_condition = True

    elif city == 'Varna' or city == 'Burgas':
        if package == 'noBreakfast':
            if vip_card == 'yes':
                price = 100 * 0.93
            elif vip_card == 'no':
                price = 100

        elif package == 'withBreakfast':
            if vip_card == 'yes':
                price = 130 * 0.88
            elif vip_card == 'no':
                price = 130

        else:
            invalid_input_condition = True

    else:
        invalid_input_condition = True

total_price = price * nights
if days_negative_condition:
    print('Days must be positive number!')
else:
    if invalid_input_condition:
        print('Invalid input!')
    else:
        print(f'The price is {total_price:.2f}lv! Have a nice time!')