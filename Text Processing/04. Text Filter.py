banned_words = input().split(", ")
string = input()
for words in banned_words:
    while words in string:
        string = string.replace(words, "*" * len(words))
print(string)