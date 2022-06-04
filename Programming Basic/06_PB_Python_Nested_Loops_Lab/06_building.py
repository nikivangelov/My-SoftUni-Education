floor_number = int(input())
apartment_number = int(input())
flat_letter = ''
for i in range(floor_number, 0, -1):
    for j in range(0, apartment_number):
        if i == floor_number:
            print(f'L{i}{j} ', end='')
        elif i % 2 == 0:
            print(f'O{i}{j} ', end='')
        elif i % 2 == 1:
            print(f'A{i}{j} ', end='')
    print()