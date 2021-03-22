first_word = input()
second_word = input()
result = ''
previous_result = first_word

for index_1 in range(len(first_word)):
    for index_2 in range(0, index_1 + 1):
        result += second_word[index_2]
    for index_3 in range(index_1 + 1, len(first_word)):
        result += first_word[index_3]
    if not result == previous_result:
        print(result)
    previous_result = result
    result = ""
