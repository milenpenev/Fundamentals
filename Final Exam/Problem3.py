data = input()
emails = {}

while not data == "Statistics":
    data = data.split("->")
    command = data[0]
    username = data[1]
    if command == "Add":
        if username in emails:
            print(f"{username} is already registered")
        else:
            emails[username] = []
    elif command == "Send":
        email = data[2]
        emails[username].append(email)
    elif command == "Delete":
        if username in emails:
            del emails[username]
        else:
            print(f"{username} not found!")
    data = input()
print(f"Users count: {len(emails)}")
sorted_emails = sorted(emails.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
for user, email in sorted_emails:
    print(f"{user}")
    for x in email:
        print(f" - {x}")