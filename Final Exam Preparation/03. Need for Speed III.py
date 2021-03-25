n = int(input())

cars = {}

for _ in range(n):
    data = input()
    car, mileage, fuel = data.split("|")
    cars[car] = {"mileage": int(mileage), "fuel": int(fuel)}
data = input()
while not data == "Stop":
    data = data.split(" : ")
    command = data[0]
    if command == "Drive":
        car = data[1]
        distance = int(data[2])
        fuel = int(data[3])
        if cars[car]["fuel"] >= fuel:
            cars[car]["fuel"] -= fuel
            cars[car]["mileage"] += distance
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if cars[car]["mileage"] >= 100000:
                cars.pop(car)
                print(f"Time to sell the {car}!")
        else:
            print(f"Not enough fuel to make that ride")
    elif command == "Refuel":
        car = data[1]
        fuel = int(data[2])
        if cars[car]["fuel"] + fuel >= 75:
            refilled_fuel = 75 - cars[car]["fuel"]
            print(f"{car} refueled with {refilled_fuel} liters")
            cars[car]["fuel"] = 75
        else:
            cars[car]["fuel"] += fuel
            print(f"{car} refueled with {fuel} liters")
    elif command == "Revert":
        car = data[1]
        distance = int(data[2])
        if cars[car]["mileage"] - distance < 10000:
            cars[car]["mileage"] = 10000
        else:
            cars[car]["mileage"] -= distance
            print(f"{car} mileage decreased by {distance} kilometers")
    data = input()
sorted_cars = {k: v for k, v in sorted(cars.items(), key= lambda tkvp: (-tkvp[1]['mileage'], tkvp[0]))}

for car in sorted_cars:
    print(f"{car} -> Mileage: {sorted_cars[car]['mileage']} kms, Fuel in the tank: {sorted_cars[car]['fuel']} lt.")