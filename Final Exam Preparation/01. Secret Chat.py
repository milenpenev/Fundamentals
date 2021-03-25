encrypted_message = input()

data = input()

while not data == "Reveal":
    data = data.split(":|:")
    command = data[0]

    if command == "InsertSpace":
        index = int(data[1])
        encrypted_message = encrypted_message[:index] + " " + encrypted_message[index:]
        print(encrypted_message)
    elif command == "Reverse":
        substring = data[1]
        if substring in encrypted_message:
            reverse_substring = substring[::-1]
            encrypted_message = encrypted_message.replace(substring, "", 1)
            encrypted_message = encrypted_message + reverse_substring
            print(encrypted_message)
        else:
            print("error")
    elif command == "ChangeAll":
        substring = data[1]
        replacement = data[2]
        encrypted_message = encrypted_message.replace(substring, replacement)
        print(encrypted_message)
    data = input()
print(f"You have a new text message: {encrypted_message}")