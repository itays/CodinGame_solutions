import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

road = int(raw_input())  # the length of the road before the gap.
gap = int(raw_input())  # the length of the gap.
platform = int(raw_input())  # the length of the landing platform.

# game loop
while True:
    speed = int(raw_input())  # the motorbike's speed.
    coord_x = int(raw_input())  # the position on the road of the motorbike.
    """
    print >> sys.stderr, 'road: ' + str(road)
    print >> sys.stderr, 'platform: ' + str(platform)
    print >> sys.stderr, 'gap: ' + str(gap)
    print >> sys.stderr, 'coord_x: ' + str(coord_x)
    print >> sys.stderr, 'speed: ' + str(speed)
    """
    
    if coord_x == road - 1:
        print "JUMP"
    elif coord_x > road - 1:
        print "SLOW"
    elif speed == gap + 1:
        print "WAIT"
    elif speed > gap + 1:
        print "SLOW"
    else:
        print "SPEED"
        
    
    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."
    
    # A single line containing one of 4 keywords: SPEED, SLOW, JUMP, WAIT.
    #print action
