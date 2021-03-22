numbers = [int(el) for el in input().split(", ")]

group = 10
numbers_group = []
max_number = max(numbers)

while numbers:

    for num in numbers:
        if num in range(group - 10, group +1):
            numbers_group.append(num)
    for num in numbers_group:
        numbers.remove(num)
    print(f"Group of {group}'s: {numbers_group}")
    numbers_group = []
    group += 10
