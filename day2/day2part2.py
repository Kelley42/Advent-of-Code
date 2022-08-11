L = 0
W = 0
H = 0

def findRibbonLength():
    ribbon_lengths = []
    ribbon_lengths.extend([L, W, H])
    ribbon_lengths.sort()
    return (2*ribbon_lengths[0]) + (2*ribbon_lengths[1])

def findBowLength():
    return L*W*H

total_ribbon_length = 0
total_bow_length = 0
with open("day2.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
    for entry in lines:
        L, W, H = [int(x) for x in entry.split("x")]
        total_ribbon_length += findRibbonLength()
        total_bow_length += findBowLength()

print(total_ribbon_length + total_bow_length)