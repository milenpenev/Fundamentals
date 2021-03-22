elements = input().split()
products = {}
for i in range(0, len(elements), 2):
    key = elements[i]
    value = elements[i + 1]
    products[key] = int(value)

searched_products = input().split()

for s_product in searched_products:
    if s_product not in products:
        print(f"Sorry, we don't have {s_product}")
    else:
        print(f"We have {products[s_product]} of {s_product} left")