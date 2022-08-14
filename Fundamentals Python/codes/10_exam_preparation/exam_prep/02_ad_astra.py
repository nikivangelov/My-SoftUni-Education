import re

input_message = input()
pattern = r"([#\|])([A-Za-z\s]+)(\1)(\d{2})(\/)(\d{2})(\5)(\d{2})(\1)(\d+)(\1)"
matches = re.findall(pattern, input_message)
calories = 0
whole_list = []
for item in matches:
    item_list = []
    item_name = item[1]
    item_list.append(item_name)
    exp_date = ''
    current_calories = 0
    for i in range(3, 8):
        exp_date += item[i]
    item_list.append(exp_date)
    current_calories = int(item[-2])
    calories += current_calories
    item_list.append(current_calories)
    # print(item_dict)
    whole_list.append(item_list)
print(f"You have food to last you for: {int(calories/2000)} days!")
for current_item in whole_list:
    item_name = current_item[0]
    item_exp_date = current_item[1]
    item_calories = int(current_item[2])
    print(f"Item: {item_name}, Best before: {item_exp_date}, Nutrition: {item_calories}")