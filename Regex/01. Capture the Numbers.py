import re
text = input()

pattern = r"\d+"

numbers = []

while text:
    matches = re.findall(pattern, text)
    numbers.extend(matches)
    text = input()

print(*numbers)