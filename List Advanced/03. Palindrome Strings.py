words = input().split()
searched_palindrome = input()
counter = 0

list_of_palindromes = [el for el in words if el == el[::-1]]
for searching in words:
    if searched_palindrome == searching:
        counter += 1

print(list_of_palindromes)
print(f"Found palindrome {counter} times")