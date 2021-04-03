import re

n = int(input())
pattern = r"(?P<start_sep>\*|@)(?P<word>[A-Z][a-z]{2,})(?P=start_sep): (\[|\])(?P<letter1>[A-Za-z])(\[|\])(\|)(\[|\])" \
          r"(?P<letter2>[A-Za-z])(\[|\])(\|)(\[|\])(?P<letter3>[A-Za-z])(\[|\])(\|)$"

for _ in range(n):
    string = input()
    matches = [el.groupdict() for el in re.finditer(pattern, string)]
    if not matches:
        print("Valid message not found!")
    else:
        for match in matches:
            print(f"{match['word']}: {ord(match['letter1'])} {ord(match['letter2'])} {ord(match['letter3'])}")