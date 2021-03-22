n = int(input())

students = {}

for _ in range(n):
    name = input()
    grade = float(input())
    if name not in students:
        students[name] = []
    students[name].append(grade)

filtered_students = {}
for student_name, grades in students.items():
    avg_grade = sum(grades) / len(grades)
    if avg_grade >= 4.50:
        filtered_students[student_name] = avg_grade

sorted_best_students = sorted(filtered_students.items(), key=lambda kvp: kvp[1], reverse=True)

for student, grade in sorted_best_students:
    print(f"{student} -> {grade:.2f}")