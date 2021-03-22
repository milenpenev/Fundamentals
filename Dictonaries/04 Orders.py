data = input()

orders = {}
total_price = 0

while not data == "buy":
    name, price, quantity = data.split()
    price = float(price)
    quantity = float(quantity)
    if name not in orders:
        orders[name] = {"price": price, "quantity": quantity}
    else:
        orders[name]["price"] = price
        orders[name]["quantity"] += quantity
    data = input()
for name in orders:
    print(f"{name} -> {orders[name]['price'] * orders[name]['quantity']:.2f}")