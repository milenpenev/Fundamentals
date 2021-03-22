initial_energy = int(input())
command = input()

won_battles = 0

while not command == "End of battle":
    if initial_energy - int(command) >= 0:
        won_battles += 1
        initial_energy -= int(command)
        if won_battles % 3 == 0:
            initial_energy += won_battles
    else:
        print(f"Not enough energy! Game ends with {won_battles} won battles and {initial_energy} energy")
        break
    command = input()
if command == "End of battle":
    print(f"Won battles: {won_battles}. Energy left: {initial_energy}")