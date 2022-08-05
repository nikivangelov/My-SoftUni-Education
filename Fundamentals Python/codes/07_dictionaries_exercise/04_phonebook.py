n = 0
phonebook = {}
while True:
    contact = input().split('-')
    if len(contact) < 2:
        n = int(contact[0])
        break
    name = contact[0]
    phone_number = contact[1]
    phonebook[name] = phone_number

for i in range(n):
    current_name = input()
    if current_name not in phonebook:
        print(f"Contact {current_name} does not exist.")
    else:
        print(f"{current_name} -> {phonebook[current_name]}")


