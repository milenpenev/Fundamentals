n = int(input())

list_of_positive = []
list_of_negative = []
sum_of_negatives = 0

for numbers in range(n):
    number = int(input())
    if number >= 0:
        list_of_positive.append(number)
    elif number < 0:
        list_of_negative.append(number)
        sum_of_negatives += number
print(list_of_positive)
print(list_of_negative)
print(f"Count of positives: {len(list_of_positive)}. Sum of negatives: {sum_of_negatives}")