divisor = int(input())
bound = int(input())

for number in range(bound, divisor, -1):
    if number % divisor == 0 and number > 0:
        print(number)
        break