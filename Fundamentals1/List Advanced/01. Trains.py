number_of_wagons = int(input())
wagons = []

for wagon in range(number_of_wagons):
    wagons.append(0)

command = input().split()

while not command[0] == "End":
    #command_int = list(map(int, command))
    if command[0] == "add":
        wagons[-1] += int(command[1])
    elif command[0] == "insert":
        command_index = int(command[1])
        wagons[command_index] += int(command[2])
    elif command[0] == "leave":
        command_index = int(command[1])
        wagon_people_leave = int(wagons[command_index])
        wagon_people_leave -= int(command[2])
        wagons[command_index] = wagon_people_leave
    command = input().split()
print(wagons)