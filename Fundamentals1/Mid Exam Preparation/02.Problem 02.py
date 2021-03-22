string = input().split()
command = input()

while not command == "end":
    command = command.split(" ")
    if command[0] == "reverse" or command[0] == "sort":
        start = int(command[2])
        count = int(command[4])
    else:
        count = int(command[1])
    if command[0] == "reverse":
        index_end = start + count
        string[start:index_end] = string[start:index_end][::-1]
    elif command[0] == "sort":
        index_end = start + count
        string[start:index_end] = sorted(string[start:index_end])
    elif command [0] == "remove":
        for el in range(count):
            string.pop(0)
    command = input()
print(", ".join(string))
