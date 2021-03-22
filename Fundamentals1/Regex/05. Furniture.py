import re

text = input()

pattern = r">>(?P<names>[a-zA-z]+)<<(?P<price>\d+(\.\d+)?)\!(?P<quantity>\d+)"
total_sum = 0
matches = []
while not text == "Purchase":
    valid_data = re.match(pattern, text)
    if valid_data:
        data = valid_data.groupdict()
        matches.append(data['names'])
        total_sum += float(data['price']) * int(data['quantity'])
    text = input()
print("Bought furniture:")
if matches:
    print("\n".join(matches))
print(f"Total money spend: {total_sum:.2f}")