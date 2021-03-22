def loaded_percentage(number):
    loaded_bar = [".", ".", ".", ".", ".", ".", ".", ".", ".", "."]
    n = number // 10
    for loading in range(n):
        loaded_bar[loading] = "%"
    return loaded_bar


percentage = int(input())
bar_result = loaded_percentage(percentage)
string = ""
if percentage == 100:
    print(f"{percentage}% Complete!")
    print(f"[{string.join(bar_result)}]")
else:
    print(f"{percentage}% [{string.join(bar_result)}]")
    print("Still loading...")