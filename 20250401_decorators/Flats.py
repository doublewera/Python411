from random import randint
from Flat import Flat, Room

flats = []
for i in range(10):
    N = randint(1, 4)
    flat = []
    for r in range(N):
        flat.append(Room(
            randint(3, 6), #
            randint(3, 6)
        ))
    flats.append(Flat(flat))

for f in flats:
    print(f)

result = {}
for f in flats:
    room_count = f.room_number()
    if not (room_count in result):
        result[room_count] = []
    result[room_count].append(f)

for count in result:
    print('\n\n', count)
    for f in result[count]:
        print(f)