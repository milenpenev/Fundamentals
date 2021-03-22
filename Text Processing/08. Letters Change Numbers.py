string = input().split()

alphabet = {
        'a' : 1,
        'b' : 2,
        'c' : 3,
        'd' : 4,
        'e' : 5,
        'f' : 6,
        'g' : 7,
        'h' : 8,
        'i' : 9,
        'j' : 10,
        'k' : 11,
        'l' : 12,
        'm' : 13,
        'n' : 14,
        'o' : 15,
        'p' : 16,
        'q' : 17,
        'r' : 18,
        's' : 19,
        't' : 20,
        'u' : 21,
        'v' : 22,
        'w' : 23,
        'x' : 24,
        'y' : 25,
        'z' : 26
    }
result = 0
numbers_list = []
for combination in string:
    for char in combination:
        for numbers in combination:
            if numbers.isdigit():
                numbers_list.append(numbers)

        a_string = "".join(numbers_list)
        number = int(a_string)

        if 65 <= ord(char) <= 90 and char == combination[0]:
            result += int(number) / alphabet[char.lower()]
        elif 97 <= ord(char) <= 122 and char == combination[0]:
            result += int(number) * alphabet[char.lower()]
        elif 65 <= ord(char) <= 90 and not char == combination[0]:
            result -= alphabet[char.lower()]
        elif 97 <= ord(char) <= 122 and not char == combination[0]:
            result += alphabet[char.lower()]
        numbers_list = []
print(f"{result:.2f}")