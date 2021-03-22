data = input()
dictionary = {}

while not data == "stop":
    quantity = int(input())
    if data not in dictionary:
        dictionary[data] = 0
    dictionary[data] += quantity
    data = input()

for key, value in dictionary.items():
    print(f"{key} -> {value}")