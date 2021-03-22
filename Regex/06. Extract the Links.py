import re

text = input()
pattern = r"w{3}\.[a-zA-Z0-9-]+(\.[a-z]+)+"
valid_sites = []

while text:
    matches = [el.group() for el in re.finditer(pattern, text)]
    if matches:
        valid_sites.extend(matches)
    text = input()
print(*valid_sites, sep="\n")