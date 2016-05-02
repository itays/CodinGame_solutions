import sys
import math
from functools import cmp_to_key

n = int(input())  # the number of temperatures to analyse
temps = input()  # the n temperatures expressed as integers ranging from -273 to 5526

def comp(a, b):
    return abs(int(a)) - abs(int(b)) or int(b) - int(a)

sortedTemps = temps.split(' ')
sortedTemps.sort(key=cmp_to_key(comp))

print(sortedTemps[0] or 0)

# N = int(input())  # the number of temperatures to analyse
# # the N temperatures integers ranging from -273 to 5526
# TEMPS = [int(temp) for temp in input().split()]

# try:
#     print(sorted(sorted(TEMPS, reverse=True), key=lambda x: abs(x))[0])
# except IndexError:
#     print(0)
