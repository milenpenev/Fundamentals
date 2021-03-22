n = int(input())

list = []

for i in range(n):
    numbers = int(input())
    list.append(numbers)

command = input()

if command == "even":
    for i in range(len(list) -1, -1, -1):
        element = list[i]
        element_as_integer = int(element)
        if not element_as_integer % 2 == 0:
            list.remove(element)
elif command == "odd":
    for i in range(len(list) -1, -1, -1):
        element = list[i]
        element_as_integer = int(element)
        if element_as_integer % 2 == 0:
            list.remove(element)
elif command == "negative":
    for i in range(len(list) -1, -1, -1):
        element = list[i]
        element_as_integer = int(element)
        if element_as_integer >= 0:
            list.remove(element)
elif command == "positive":
    for i in range(len(list) -1, -1, -1):
        element = list[i]
        element_as_integer = int(element)
        if element_as_integer < 0:
            list.remove(element)
print(list)