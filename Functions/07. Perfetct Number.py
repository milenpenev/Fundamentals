def is_number_perfect(num):
    sum_of_devisors = 0
    for el in range(1, num):
        if num % el == 0:
            sum_of_devisors += el
    if sum_of_devisors == num:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


number = int(input())
result = is_number_perfect(number)
print(result)