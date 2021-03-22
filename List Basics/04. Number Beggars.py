numbers = input()
result = numbers.split(", ")
beggars = int(input())
beggar_list = []
beggars_count = 0

for index in range(beggars):
    beggar_list.append(0)

for i in range(len(result)):
    result_int = int(result[i])
    result[i] = result_int
if beggars == len(result):
    print(result)
elif beggars > len(result):
    for _ in range(beggars - len(result)):
        result.append(0)
    print(result)
elif beggars < len(result):
    for el in result:
        beggar_list[beggars_count] += el
        beggars_count += 1
        if beggars_count == beggars:
            beggars_count = 0
    print(beggar_list)
