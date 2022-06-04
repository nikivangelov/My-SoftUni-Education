n = int(input())
for i in range(n):
    new_string = input()
    if ',' not in new_string and '.' not in new_string  and '_' not in new_string:
        print(f"{new_string} is pure.")
    else:
        print(f"{new_string} is not pure!")