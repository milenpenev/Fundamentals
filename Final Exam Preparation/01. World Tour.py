stops = input()
data = input()

while not data == "Travel":
    data = data.split(":")
    command = data[0]
    if command == "Add Stop":
        index = int(data[1])
        if len(stops) >= index:
            new_stop = data[2]
            stops = stops[:index] + new_stop + stops[index:]
        print(stops)
    elif command == "Remove Stop":
        left_index = int(data[1])
        right_index = int(data[2]) + 1
        if len(stops) >= left_index and len(stops) >= right_index:
            stops = stops[:left_index] + stops[right_index:]
        print(stops)
    elif command == "Switch":
        searched_destination = data[1]
        new_destination = data[2]
        if not searched_destination == new_destination:
            if searched_destination in stops:
                stops = stops.replace(searched_destination, new_destination)
        print(stops)

    data = input()

print(f"Ready for world tour! Planned stops: {stops}")