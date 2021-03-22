def is_palindrome(numbers):
    if numbers == numbers[::-1]:
        return True
    return False


list_of_numbers = input().split(", ")

for nums_as_string in list_of_numbers:
    print(is_palindrome(nums_as_string))