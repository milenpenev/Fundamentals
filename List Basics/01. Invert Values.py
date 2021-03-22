string = input()
result = string.split(" ")
new_list = []


for i in result:
    result_as_int = int(i)
    new_string = result_as_int * -1
    new_list.append(new_string)




print(new_list)