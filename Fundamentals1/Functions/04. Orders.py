def food(type, quantity):
    price = 0
    if type == "coffee":
        price = quantity * 1.5
    elif type == "water":
        price = quantity * 1
    elif type == "coke":
        price = quantity * 1.4
    elif type == "snacks":
        price = quantity * 2
    return price


type_of_food = input()
quantity_of_food = int(input())
print(f"{food(type_of_food, quantity_of_food):.2f}")
