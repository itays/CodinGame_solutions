import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in raw_input().split()]

# game loop
while True:
    remaining_turns = int(raw_input())  # The remaining amount of turns Thor can move. Do not remove this line.

    # Write an action using print
    x = ""
    y = ""
    
    if initial_ty > light_y:
        y = "N"
        initial_ty -= 1
    elif initial_ty < light_y:
        y = "S"
        initial_ty += 1
    
    if initial_tx > light_x:
        x = "W"
        initial_tx -= 1
    elif initial_tx < light_x:
        x = "E"
        initial_tx += 1
    
    move = y+x

    # A single line providing the move to be made: N NE E SE S SW W or NW
    print move
