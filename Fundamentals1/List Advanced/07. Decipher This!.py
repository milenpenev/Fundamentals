message_list = input().split()


for word in message_list:
    number = ""
    for char in word:
        if char.isdigit():
            number += char
    first_letter = chr(int(number))
    current_word = first_letter + word[len(number):]
    current_word = list(current_word)
    current_word[1], current_word[-1] = current_word[-1], current_word[1]
    print("".join(current_word), end=" ")
