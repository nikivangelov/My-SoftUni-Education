N_lines = int(input())
sum = 0
if 1 <= N_lines <= 20:
    for i in range(1, N_lines + 1):
        letter = input()
        sum += ord(letter)

    print(f"The sum equals: {sum}")