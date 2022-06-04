width = int(input())
lenght = int(input())
height = int(input())
storage_volume = width * lenght * height
free_space = 0
box_volume = 0
condition = False
while box_volume <= storage_volume:
    boxes = input()
    if boxes == 'Done':
        print(f'{abs(free_space)} Cubic meters left.')
        condition = True
        break

    box_volume += int(boxes)
    free_space = storage_volume - box_volume


if not condition:
    print(f'No more free space! You need {abs(free_space)} Cubic meters more.')