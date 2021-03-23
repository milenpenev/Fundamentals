import re

string = input()

destinations = []
total_length = 0

pattern = r"(?P<separator>(=|/))(?P<destination>[A-Z][A-Za-z][A-Za-z]+)(?P=separator)"

matches = [el.groupdict() for el in re.finditer(pattern, string)]
for match in matches:
    destinations.append(match["destination"])
    total_length += len(match["destination"])
print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {total_length}")