data = input()

users = {}

while not data == "End":
    company_name, employee_id = data.split(" -> ")
    if company_name not in users:
        users[company_name] = []
    if employee_id in users[company_name]:
        data = input()
        continue
    else:
        users[company_name].append(employee_id)
    data = input()

users_sorted = dict(sorted(users.items(), key=lambda item: item[0]))

for company in users_sorted:
    print(company)
    for employee_id in users_sorted[company]:
        print(f"-- {employee_id}")
