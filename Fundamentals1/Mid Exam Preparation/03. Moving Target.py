targets = [int(el) for el in input().split()]

command = input()

while not command == "End":
    command, index, power_radius_value = command.split()
    index = int(index)
    power_radius_value = int(power_radius_value)
    if command == "Shoot":
        if index in range(len(targets)):
            targets[index] -= power_radius_value
            if targets[index] <= 0:
                targets.pop(index)
    elif command == "Strike":
        left_most_index = index - power_radius_value
        right_most_index = index + power_radius_value
        if index in range(len(targets)) and left_most_index in range(len(targets)) and right_most_index in range(len(targets)):
            left_unstriked_index = targets[:left_most_index]
            right_unstriked_index = targets[right_most_index + 1:]
            targets = left_unstriked_index + right_unstriked_index
        else:
            print("Strike missed!")
    elif command == "Add":
        if index in range(len(targets)):
            targets.insert(index, power_radius_value)
        else:
            print("Invalid placement!")
    command = input()

print("|".join([str(el) for el in targets]))
