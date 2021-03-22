multiplier = int(input())
count = int(input())
list_of_numbers = []

for numbers in range(1, count +1):
    nums = numbers * multiplier
    list_of_numbers.append(nums)
print(list_of_numbers)