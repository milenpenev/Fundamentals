data = input()

key_materials = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}
legendary_items = {"shards": 0, "fragments": 0, "motes": 0}
junk_items = {}
is_legendary_item_reached = False

while not is_legendary_item_reached:

    split_data = data.split()
    for kvp in range(0, len(split_data), 2):
        if is_legendary_item_reached:
            break
        material = split_data[kvp + 1].lower()
        value = int(split_data[kvp])
        if material in legendary_items:
            legendary_items[material] += value
        else:
            if material in junk_items:
                junk_items[material] += value
            else:
                junk_items[material] = value
        for material, value in legendary_items.items():
            if value >= 250:
                is_legendary_item_reached = True
                print(f"{key_materials[material]} obtained!")
                legendary_items[material] -= 250
                break
    if is_legendary_item_reached:
        break
    data = input()

junk_items = sorted(junk_items.items(), key=lambda item: item[0])
legendary_items_sorted = sorted(legendary_items.items(), key=lambda item: (-item[1], item[0]))
for key, value in legendary_items_sorted:
    print(f"{key}: {value}")
for key, value in junk_items:
    print(f"{key}: {value}")