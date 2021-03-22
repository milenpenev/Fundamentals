def odd_or_even_sum(nums):
    sum_of_odd = 0
    sum_of_even = 0
    for el in str(nums):
        num_as_int = int(el)
        if num_as_int % 2 == 0:
            sum_of_even += num_as_int
        else:
            sum_of_odd += num_as_int
    return sum_of_odd, sum_of_even


numbers = int(input())
result = odd_or_even_sum(numbers)
print(f"Odd sum = {result[0]}, Even sum = {result[1]}")