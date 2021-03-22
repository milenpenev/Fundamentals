string = input()

list_of_chars = []
last_char = ""
for char in string:
    if not char == last_char:
        list_of_chars.append(char)
        last_char = char
    else:
        print("".join(list_of_chars), end="")
        list_of_chars = []
print("".join(list_of_chars))
