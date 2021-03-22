def smallest_number(first, second, third):
    if first < second and first < third:
        return first
    elif second < first and second < third:
        return second
    elif third < first and third < second:
        return third


first_number = int(input())
second_number = int(input())
third_number = int(input())

print(smallest_number(first_number, second_number, third_number))
