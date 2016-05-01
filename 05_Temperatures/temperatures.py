import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(raw_input())  # the number of temperatures to analyse
temps = raw_input()  # the n temperatures expressed as integers ranging from -273 to 5526


def compare(a, b):
    return abs(int(a)) - abs(int(b)) or int(b) - int(a)
    
sortedTemps = temps.split(' ')
sortedTemps.sort(compare)

print sortedTemps[0] or 0