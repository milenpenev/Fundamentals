encrypted_string = input()

data = input()

while not data == "Decode":
    data = data.split("|")
    command = data[0]
    if command == "Move":
        number_of_letters = int(data[1])
        encrypted_string = encrypted_string[number_of_letters:] + encrypted_string[:number_of_letters]
    elif command == "Insert":
        index = int(data[1])
        value = data[2]
        encrypted_string = encrypted_string[:index] + value + encrypted_string[index:]
    elif command == "ChangeAll":
        substring = data[1]
        replacement = data[2]
        encrypted_string = encrypted_string.replace(substring, replacement)
    data = input()
print(f"The decrypted message is: {encrypted_string}")