L = 0
W = 0
H = 0

def findArea():
    side_array = []
    side1 = L*W
    side2 = W*H
    side3 = L*H
    side_array.extend([side1, side2, side3])
    min_side = min(side_array)
    return (2*side1) + (2*side2) + (2*side3) + min_side

total_area = 0
with open("day2.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
    for entry in lines:
        L, W, H = [int(x) for x in entry.split("x")]
        total_area += findArea()

print(total_area)
        

