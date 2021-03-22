string = input()

numbers = ""
letters = ""
others = ""

for char in string:
    if char.isnumeric():
        numbers += char
    elif char.isalpha():
        letters += char
    else:
        others += char
print(numbers)
print(letters)
print(others)
