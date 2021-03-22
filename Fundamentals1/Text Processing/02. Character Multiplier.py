strings = input().split()
max_length = max(strings, key=len)
min_length = min(strings, key=len)
first_word = strings[0]
second_word = strings[1]
total_sum = 0
for first_index in range(len(max_length)):
    if first_index in range(len(min_length)):
        total_sum += ord(first_word[first_index]) * ord(second_word[first_index])
    elif first_index in range(len(first_word)):
        total_sum += ord(first_word[first_index])
    elif first_index in range(len(second_word)):
        total_sum += ord(second_word[first_index])

print(total_sum)