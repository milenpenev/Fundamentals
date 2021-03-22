import re
numbers = input()

pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"

matches = [number.group() for number in re.finditer(pattern, numbers)]
print(*matches)