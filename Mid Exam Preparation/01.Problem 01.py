orders = int(input())

total_price = 0

for order in range(orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules = int(input())
    price_per_coffee = ((days * capsules) * price_per_capsule)
    total_price += price_per_coffee
    print(f"The price for the coffee is: ${price_per_coffee:.2f}")
    price_per_coffee = 0
print(f"Total: ${total_price:.2f}")