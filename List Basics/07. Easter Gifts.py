gift_names = input().split()
command = input()

while not command == "No Money":
    current_command = command.split()
    current_gift = current_command[1]
    if current_command[0] == "OutOfStock":
        for index in range(len(gift_names)):
            if gift_names[index] == current_gift:
                gift_names[index] = "None"
    elif current_command[0] == "Required":
        index = int(current_command[2])
        if 0 <= index <= len(gift_names):
            gift_names[index] = current_gift
    elif current_command[0] == "JustInCase":
        gift_names[-1] = current_gift
    command = input()
for gift in gift_names:
    if not gift == "None":
        print(gift, end=" ")