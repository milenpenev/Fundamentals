import re
text = input()

pattern = r"\+359(?P<separators> |-)2(?P=separators)\d{3}(?P=separators)\d{4}\b"

matches = [phone.group() for phone in re.finditer(pattern, text)]
print(", ".join(matches))