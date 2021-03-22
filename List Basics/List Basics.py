# list_example = ["apple", "banana", "orange"]
# result = ' '.join(list_example)
#
#
# print(result)
# #
# word = "Hello"
# #
# list_example_2 = list(word)
# result_2 = ''.join(list_example_2)
# print(result_2)
#
# word = "Hello"
# word_as_list = list(word)
#
# for el in word_as_list:
#     print(el)
#
# print("")
# numbers = [100, 102, 103, 104, 105]
#
# for i in range(len(numbers)):
#      print(chr(numbers[i]))

cards = input().split()

A = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
B = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']

isTerminated = False

for card in cards:
    current_card = card.split('-')
    # if not current_card[-1] in A or not current_card[-1] in B:
    #     continue
    if current_card[0] == "A":
        A.remove(current_card[-1])
    else:
        B.remove(current_card[-1])
    if len(A) < 7 or len(B) < 7:
        isTerminated = True
        break
print(f'Team A - {len(A)}; Team B - {len(B)}')
if isTerminated:
    print('Game was terminated')