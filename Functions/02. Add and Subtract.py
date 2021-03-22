def sum_numbers(num1, num2):
    result_sum = num1 + num2
    return result_sum


def subtract(num1_and_num2, num3):
    result_subtract = num1_and_num2 - num3
    return result_subtract


first_number = int(input())
second_number = int(input())
third_number = int(input())

result_of_sum = sum_numbers(first_number, second_number)
result_of_subtract = subtract(result_of_sum, third_number)
print(result_of_subtract)