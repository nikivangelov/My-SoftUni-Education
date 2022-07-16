rooms = int(input())
left_chairs = 0
enough_chairs_in_every_room = True
for room in range(rooms):
    command = input().split(' ')
    current_chairs = len(command[0])
    visitors = int(command[1])
    current_result = current_chairs - visitors
    if current_result >=0:
        left_chairs += current_result
    else:
        print(f"{abs(current_result)} more chairs needed in room {int(room)+1}")
        enough_chairs_in_every_room = False

if enough_chairs_in_every_room:
    print(f"Game On, {left_chairs} free chairs left")

