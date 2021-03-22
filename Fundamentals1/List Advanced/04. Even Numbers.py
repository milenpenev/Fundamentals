nums = input().split(", ")
nums_int = list(map(int, nums))
indexes = []
for i in range(len(nums_int)):
    if nums_int[i] % 2 == 0:
        indexes.append(i)
print(indexes)