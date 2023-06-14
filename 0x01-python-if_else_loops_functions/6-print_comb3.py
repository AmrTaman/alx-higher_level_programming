#!/usr/bin/python3
print("01", end='')
for x in range(10):
    for y in range(x+1, 10):
        if x == 0 and y == 1:
            continue
        print(", {}{}".format(x, y), end='')
print()
