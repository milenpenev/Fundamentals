string = input()
data = input()
result = ""

while not data == "Done":
    data = data.split()
    command = data[0]
    if command == "TakeOdd":
        for index in range(len(string)):
            if not index % 2 == 0:
                result += string[index]
        print(result)
        string = result
    result = ""
    if command == "Cut":
        index = int(data[1])
        length = int(data[2])
        result = string[index: index + length]
        string = string.replace(result, "", 1)
        print(string)
    if command == "Substitute":
        substring = data[1]
        substitute = data[2]
        if substring in string:
            string = string.replace(substring, substitute)
            print(string)
        else:
            print("Nothing to replace!")
    data = input()
print(f"Your password is: {string}")