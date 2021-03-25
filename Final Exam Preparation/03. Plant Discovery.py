n = int(input())
dict_to_be_sorted = {}
dict_with_avg_ratings = {}
plants = {}
plants_ratings = {}
for plant in range(n):
    new_plant, rarity = input().split("<->")
    plants[new_plant] = int(rarity)
data = input()

while not data == "Exhibition":
    data = data.split(": ")
    command = data[0]
    if not command == "Reset":
        current_plant, rating = data[1].split(" - ")
        rating = int(rating)
    if command == "Reset":
        plants_ratings[data[1]] = 0
    elif command == "Rate":
        if current_plant not in plants_ratings:
            plants_ratings[current_plant] = [rating]
        else:
            plants_ratings[current_plant].append(rating)
    elif command == "Update":
        plants[current_plant] = rating
    else:
        print("error")
    data = input()

print("Plants for the exhibition:")
for plant in plants:
    if not plants_ratings[plant] == 0:
        avg_rating = sum(plants_ratings[plant]) / len(plants_ratings[plant])
    else:
        avg_rating = 0
    if plant not in dict_with_avg_ratings:
        dict_with_avg_ratings[plant] = avg_rating

sorted_dict_with_ratings = {k: v for k, v in sorted(plants.items(), key=lambda item: -item[1])}
for el in sorted_dict_with_ratings:
    print(f"- {el}; Rarity: {sorted_dict_with_ratings[el]}; Rating: {dict_with_avg_ratings[el]:.2f}")