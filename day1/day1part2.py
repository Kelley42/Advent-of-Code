floor = 0
count = 0
with open("day1.txt") as file:
    contents = file.read()
    for entry in contents:
        if floor == -1:
            print("stop!")
            print(count)
            break
        if entry == "(":
            floor += 1
            count += 1
        elif entry == ")":
            floor -= 1
            count += 1
        

