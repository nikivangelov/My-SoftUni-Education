n = int(input())
for i in range(n):
    opposite_string = input()
    if ',' not in opposite_string and '.' not in opposite_string  and '_' not in opposite_string:
        print(f"{opposite_string} is pure.")
    else:
        print(f"{opposite_string} is not pure!")