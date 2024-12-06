import re
file = open("/Users/trey/advent-of-code-2024/6/input.txt", "r")

rows = file.read().split("\n")
directions = ["N", "E", "S", "W"]
direction = "N"
x, y = 0, 0

for i in range(0, len(rows)):
    for j in range(0, len(rows[i])):
        if rows[i][j] == "^":
            x, y = j, i

distinct_steps = set()
steps_with_directions = list()
possible_loops = 0
while y >= 0 and y < len(rows) and x >= 0 and x < len(rows[0]):
    if direction == "N":
        y -= 1

        if (x+1, y+1, "E") in steps_with_directions:
                possible_loops += 1
        
        if (y >= 0):
            if (rows[y][x]) == "#":
                direction = "E"
                y += 1
            else:
                distinct_steps.add((x, y))
                steps_with_directions.append((x, y, "N"))
    elif direction == "E":
        x += 1

        if (x-1, y+1, "S") in steps_with_directions:
                possible_loops += 1

        if (x < len(rows[0])):
            if (rows[y][x]) == "#":
                direction = "S"
                x -= 1
            else:
                distinct_steps.add((x, y))
                steps_with_directions.append((x, y, "E"))
    elif direction == "S":
        y += 1

        if (x-1, y-1, "W") in steps_with_directions:
                possible_loops += 1
        
        if (y < len(rows)):
            if (rows[y][x]) == "#":
                direction = "W"
                y -= 1
            else:
                distinct_steps.add((x, y))
                steps_with_directions.append((x, y, "S"))
    elif direction == "W":
        x -= 1

        if (x+1, y-1, "N") in steps_with_directions:
                possible_loops += 1
        
        if x >= 0:
            if (rows[y][x]) == "#":
                direction = "N"
                x += 1
            else:
                distinct_steps.add((x, y))
                steps_with_directions.append((x, y, "W"))

    mat = list([])
    for i in range(0, len(rows)):
        row = ""
        for j in range(0, len(rows[i])):
            if (j, i) in distinct_steps:
                row += "X"
            else:
                row += rows[i][j]
        mat.append(row)

    for line in mat:
        print(line)
        



    
print("part one:", len(distinct_steps))
print("part one:", possible_loops)