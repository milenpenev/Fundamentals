targets = [int(index) for index in input().split()]
shot_targets = 0
shot = 0

while True:
    shot = input()
    if shot == "End":
        break
    shot = int(shot)
    if shot >= len(targets):
        continue
    for target in range(len(targets)):
        if target == shot:
            shot_targets += 1
            for every_target in range(len(targets)):
                if targets[every_target] == -1:
                    continue
                if every_target == shot:
                    continue
                if targets[every_target] > targets[target]:
                    targets[every_target] -= targets[target]
                elif targets[every_target] <= targets[target]:
                    targets[every_target] += targets[target]
            targets[target] = -1
print(f"Shot targets: {shot_targets} -> ", end="")
for index in range(len(targets)):
    print(f"{targets[index]} ", end='')