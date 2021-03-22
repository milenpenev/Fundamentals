numbers = input().split()
n = int(input())
smallest_number = 9999999999999

res = [int(i) for i in numbers]

for smallest_numbers in range(n):
    for number in res:
        if number < smallest_number:
            smallest_number = number
    res.remove(smallest_number)
    smallest_number = 9999999999999
print(res)