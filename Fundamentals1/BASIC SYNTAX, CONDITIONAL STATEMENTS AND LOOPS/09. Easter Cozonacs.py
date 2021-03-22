budget = float(input())
flour_price = float(input())

eggs_price = flour_price * 0.75
milk_price = flour_price * 1.25
colored_eggs = 0
cozonac_quantity = 0

cozonac_price = flour_price + eggs_price + milk_price * 0.25

while budget - cozonac_price > 0:
    if budget < 0:
        break
    colored_eggs += 3
    cozonac_quantity += 1
    current_cozonacs = cozonac_quantity
    if cozonac_quantity % 3 == 0:
        colored_eggs = colored_eggs - (cozonac_quantity - 2)
    budget -=cozonac_price

print(f"You made {cozonac_quantity} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")