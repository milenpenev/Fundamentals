price_ratings = [int(el) for el in input().split(" ")]
entry_point = int(input())
type_of_items = input()
left_items_price = 0
right_items_price = 0
left_side = price_ratings[:entry_point]
right_side = price_ratings[entry_point + 1:]

if type_of_items == "cheap":
    for item in left_side:
        if item < price_ratings[entry_point]:
            left_items_price += item
    for item in right_side:
        if item < price_ratings[entry_point]:
            right_items_price += item
elif type_of_items == "expensive":
    for item in left_side:
        if item >= price_ratings[entry_point]:
            left_items_price += item
    for item in right_side:
        if item >= price_ratings[entry_point]:
            right_items_price += item
if left_items_price >= right_items_price:
    print(f"Left - {left_items_price}")
elif right_items_price > left_items_price:
    print(f"Right - {right_items_price}")