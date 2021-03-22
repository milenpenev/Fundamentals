n = int(input())

parking = {}

for info in range(0, n):
    data = input().split()
    command = data[0]
    username = data[1]
    if len(data) == 3:
        license_plate = data[2]
    if username not in parking:
        if command == "register":
            parking[username] = license_plate
            print(f"{username} registered {license_plate} successfully")
        elif command == "unregister":
            print(f"ERROR: user {username} not found")
    elif username in parking:
        if command == "register":
            print(f"ERROR: already registered with plate number {license_plate}")
        elif command == "unregister":
            print(f"{username} unregistered successfully")
            parking.pop(username)
for key, value in parking.items():
    print(f"{key} => {value}")
