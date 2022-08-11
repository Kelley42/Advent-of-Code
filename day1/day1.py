floor = 0
with open("day1sample.txt") as file:
    contents = file.read()
    for entry in contents:
        if entry == "(":
            floor += 1
        elif entry == ")":
            floor -= 1

print(floor)

