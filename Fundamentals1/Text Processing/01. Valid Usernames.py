import re
usernames = input().split(", ")


for word in usernames:
    if re.match("^[A-Za-z0-9_-]*$", word) and 3 < len(word) < 16:
        print(word)