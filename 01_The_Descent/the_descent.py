import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


# game loop
while True:
    mountainIndex = 0
    highestMountain = 0
    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain, from 9 to 0.
        if mountain_h > highestMountain:
            highestMountain = mountain_h
            mountainIndex = i
    print(mountainIndex)
