data = input()

all_courses = {}

while not data == "end":
    course, student = data.split(" : ")
    if course not in all_courses:
        all_courses[course] = [student]
    else:
        all_courses[course].append(student)
    data = input()
all_courses_sorted = dict(sorted(all_courses.items(), key=lambda item: (-len(item[1]))))
for x in all_courses_sorted:
    all_courses_sorted[x].sort()
for course in all_courses_sorted:
    print(f"{course}: {len(all_courses_sorted[course])}")
    for name in all_courses_sorted[course]:
        print(f"-- {name}")