string = input().split()

for words in string:
    print(words * len(words), end="")
