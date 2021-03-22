n_rooms = int(input())
all_rooms_are_ok = True
total_free_chairs = 0
for room_num in range(1 , n_rooms + 1):
    number_of_chairs, people = input().split()
    counter = 0
    if len(number_of_chairs) < int(people):
        needed_chairs_in_room = int(people) - len(number_of_chairs)
        print(f"{needed_chairs_in_room} more chairs needed in room {room_num}")
        all_rooms_are_ok = False
    else:
        free_chairs = len(number_of_chairs) - int(people)
        total_free_chairs += free_chairs
if all_rooms_are_ok:
    print(f"Game On, {total_free_chairs} free chairs left")
