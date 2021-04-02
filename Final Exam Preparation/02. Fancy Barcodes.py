import re

pattern = r"(@#+)(?P<word>[A-Z][A-Za-z0-9]{5,}(?<=[A-Z]))(@#+)"
number_of_barcodes = int(input())
for string in range(number_of_barcodes):
    products = input()
    matches = [el.groupdict() for el in re.finditer(pattern, products)]
    barcode = ""
    if not matches:
        print("Invalid barcode")
        continue
    for match in matches:
        for chars in match["word"]:
            if chars.isdigit():
                barcode += chars
        if barcode == "":
            print("Product group: 00")
        else:
            print(f"Product group: {barcode}")
        barcode = ""