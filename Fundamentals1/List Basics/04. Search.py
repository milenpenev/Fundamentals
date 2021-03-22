n = int(input())
word = input()

list = []

for strings in range(n):
    sentances = input()
    list.append(sentances)
print(list)
for i in range(len(list) -1, -1, -1):
    element = list[i]
    if word not in element:
        list.remove(element)
print(list)