import re
string = input()
mirror_words = {}
pattern = r"(?P<separator>@|#)(?P<word1>[A-Za-z]{3,})(?P=separator)(?P=separator)(?P<word2>[A-Za-z]{3,})(?P=separator)"

matches = [word.groupdict() for word in re.finditer(pattern, string)]

if len(matches) == 0:
    print("No word pairs found!")
else:
    print(f"{len(matches)} word pairs found!")

for match in matches:
    word_1 = match["word1"]
    word_2 = match["word2"]
    if word_1 == word_2[::-1]:
        mirror_words[word_1] = word_2

if len(mirror_words) == 0:
    print(f"No mirror words!")
else:
    print("The mirror words are:")
    index = 1
    for mirrored_word_1, mirrored_word_2 in mirror_words.items():
        if index == len(mirror_words):
            print(f"{mirrored_word_1} <=> {mirrored_word_2}")
        else:
            print(f"{mirrored_word_1} <=> {mirrored_word_2}", end=", ")
            index += 1