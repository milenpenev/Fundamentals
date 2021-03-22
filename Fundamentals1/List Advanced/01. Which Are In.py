substrings = input().split(", ")
strings = input().split(", ")

# result = [substr for substr in substrings for el in range(len(strings)) if el in strings[el]]
result = []
for substr in substrings:
    for el in range(len(strings)):
        if substr in strings[el]:
            result.append(substr)

print(sorted(set(result), key=result.index))