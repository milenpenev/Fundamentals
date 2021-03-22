str1 = input()
str2 = input()

previous_result = str1
current_result = ""

for iteration in range(len(str1)):
    for index_str_2 in range(0, iteration+1):
        current_result += str2[index_str_2]
    for index_str_1 in range(iteration+1, len(str1)):
        current_result += str1[index_str_1]
    if current_result != previous_result:
        print(current_result)
    previous_result = current_result
    current_result = ""