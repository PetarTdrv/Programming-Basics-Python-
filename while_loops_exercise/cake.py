width = int(input())
lenght = int(input())
all_slices = width * lenght
pieces_counter = 0

while all_slices > pieces_counter:
    command = input()

    if command == "STOP":
        break

    person_slices = int(command)
    pieces_counter += person_slices

pieces_counter = abs(all_slices - pieces_counter)
    
if command == "STOP":
    print(f"{pieces_counter} pieces are left.")
else:
    print(f"No more cake left! You need {pieces_counter} pieces more.")
