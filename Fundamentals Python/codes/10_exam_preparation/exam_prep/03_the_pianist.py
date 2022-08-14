number_of_pieces = int(input())
piece_collection = {}
for _ in range(number_of_pieces):
    current_piece = input().split('|')
    piece_collection[current_piece[0]] = {}
    piece_collection[current_piece[0]]['Composer'] = current_piece[1]
    piece_collection[current_piece[0]]['Key'] = current_piece[2]


while True:
    command = input().split('|')
    if command[0] == 'Stop':
        break
    elif command[0] == 'Add':
        if command[1] not in piece_collection:
            print(f"{command[1]} by {command[2]} in {command[3]} added to the collection!")
            piece_collection[command[1]] = {}
            piece_collection[command[1]]['Composer'] = command[2]
            piece_collection[command[1]]['Key'] = command[3]
        else:
            print(f"{command[1]} is already in the collection!")
    elif command[0] == 'Remove':
        if command[1] in piece_collection:
            print(f"Successfully removed {command[1]}!")
            del piece_collection[command[1]]
        else:
            print(f"Invalid operation! {command[1]} does not exist in the collection.")

    elif command[0] == 'ChangeKey':
        if command[1] in piece_collection:
            print(f"Changed the key of {command[1]} to {command[2]}!")
            piece_collection[command[1]]['Key'] = command[2]
        else:
            print(f"Invalid operation! {command[1]} does not exist in the collection.")

for key in piece_collection.keys():
    print(f"{key} -> Composer: {piece_collection[key]['Composer']}, Key: {piece_collection[key]['Key']}")