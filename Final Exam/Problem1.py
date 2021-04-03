string = input()
data = input()

while not data == "Finish":

    data = data.split()
    command = data[0]
    if command == "Replace":
        current_char = data[1]
        new_char = data[2]
        string = string.replace(current_char, new_char)
        print(string)
    elif command == "Cut":
        start_index = int(data[1])
        end_index = int(data[2])
        if 0 <= start_index < len(string) and 0 <= end_index < len(string):
            string = string[:start_index] + string[end_index + 1:]
            print(string)
        else:
            print("Invalid indices!")
    elif command == "Make":
        upper_lower = data[1]
        if upper_lower == "Upper":
            string = string.upper()
            print(string)
        elif upper_lower == "Lower":
            string = string.lower()
            print(string)
    elif command == "Check":
        substring = data[1]
        if substring in string:
            print(f"Message contains {substring}")
        else:
            print(f"Message doesn't contain {substring}")
    elif command == "Sum":
        start_index = int(data[1])
        end_index = int(data[2])
        if 0 <= start_index < len(string) and 0 <= end_index < len(string):
            substring = string[start_index:end_index+1]
            result = 0
            for chars in substring:
                result += ord(chars)
            print(result)

        else:
            print("Invalid indices!")
    data = input()
