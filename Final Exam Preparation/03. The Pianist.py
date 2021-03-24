number_of_pieces = int(input())

pieces = {}

for el in range(number_of_pieces):
    data = input()
    piece, composer, key = data.split("|")
    pieces[piece] = {'Composer': composer, 'Key': key}

data = input()
while not data == "Stop":
    data = data.split("|")
    command = data[0]
    piece = data[1]
    if command == "Add":
        composer = data[2]
        key = data[3]
        if piece not in pieces:
            pieces[piece] = {'Composer': composer, 'Key': key}
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")
    elif command == "Remove":
        if piece in pieces:
            pieces.pop(piece)
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif command == "ChangeKey":
        new_key = data[2]
        if piece in pieces:
            pieces[piece]['Key'] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    data = input()

sorted_pieces = {k: v for k, v in sorted(pieces.items(), key=lambda item: item[0])}
for piece in sorted_pieces:
    print(f"{piece} -> Composer: {pieces[piece]['Composer']}, Key: {pieces[piece]['Key']}")