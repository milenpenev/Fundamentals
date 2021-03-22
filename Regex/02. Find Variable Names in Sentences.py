import re
text = input()

pattern = r"(^_|(?<=\s_))[a-zA-Z0-9]+\b"

matches = [match.group() for match in re.finditer(pattern, text)]
print(",".join(matches))