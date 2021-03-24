import re
string = input()

pattern = r"(?P<separator>#|\|)(?P<item>[A-Za-z\s]+)(?P=separator)(?P<date>\d{2}/\d{2}/\d{2})(?P=separator)(?P<calories>[0-9]+)(?P=separator)"

matches = [el.groupdict() for el in re.finditer(pattern, string)]
calories = 0
for cal in matches:
    calories += int(cal['calories'])

days_last = calories // 2000

print(f"You have food to last you for: {days_last} days!")
for match in matches:
    print(f"Item: {match['item']}, Best before: {match['date']}, Nutrition: {match['calories']}")