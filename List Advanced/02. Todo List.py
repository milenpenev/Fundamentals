command = input()
notes = ["0"] * 10

while not command == "End":
    tokens = command.split("-")
    priority = int(tokens[0]) - 1
    note = tokens[1]
    notes[priority] = note
    command = input()

result = [element for element in notes if not element == "0"]
# for element in notes:
#     if not element == "0":
#         result.append(element)
print(result)