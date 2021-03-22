words = input()
dictionary = {}

for word in words:
    if word in dictionary:
        dictionary[word] += 1
    else:
        dictionary[word] = 1
for char, quantity in dictionary.items():
    if char == " ":
        continue
    print(f"{char} -> {quantity}")