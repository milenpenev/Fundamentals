divisor = int(input())
bound = int(input())
number = 0

for i in range(divisor, bound +1):
    if i < 0:
        break
    if i % divisor == 0:
        number = i
print(number)
