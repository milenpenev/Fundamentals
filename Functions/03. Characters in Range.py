def string_of_ascii(char1, char2):
    result = ""
    for character in range(ord(char1) + 1, ord(char2)):
        result += chr(character) + " "
    return result


first_character = input()
second_character = input()


final_result = string_of_ascii(first_character, second_character)
print(final_result)