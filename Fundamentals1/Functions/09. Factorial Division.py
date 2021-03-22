def factorial(number):
    number_result = 1
    for i in range(1, number +1):
        number_result *= i
    return number_result

def factorialed_numbers_divided(result1, result2):
    divided_result = result1 / result2
    return divided_result


first_number = int(input())
second_number = int(input())

result_of_first_number = factorial(first_number)
result_of_second_number = factorial(second_number)
print(f"{factorialed_numbers_divided(result_of_first_number, result_of_second_number):.2f}")
