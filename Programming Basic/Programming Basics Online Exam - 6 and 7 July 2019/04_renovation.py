from math import ceil

height = int(input())
width = int(input())
percentage_nonpainting_area = int(input())
total_wall_area = height * width * 4
total_painting_area = total_wall_area - total_wall_area * (percentage_nonpainting_area / 100)
painting_area = 0
condition = False

while True:
    litres = input()
    if litres == 'Tired!':
        break

    painting_area += int(litres)
    if painting_area >= total_painting_area:
        condition = True
        break

diff = abs(int(painting_area - total_painting_area))
if condition:
    if diff == 0:
        print('All walls are painted! Great job, Pesho!')
    else:
        print(f'All walls are painted and you have {ceil(diff)} l paint left!')
else:
    print(f'{ceil(diff)} quadratic m left.')