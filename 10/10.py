file = open("/Users/trey/advent-of-code-2024/10/input.txt", "r")

topographic_map = []
for line in file.read().split("\n"):
    row = []
    for char in line:
        row.append(int(char))
    topographic_map.append(row)

trailheads = set()
for i in range(0, len(topographic_map)):
    for j in range(0, len(topographic_map[0])):
        if topographic_map[i][j] == 0:
            trailheads.add((i, j))

def get_trail_score(y, x, elev, nines):
    if elev == 9:
        nines.add((y, x))
        return len(nines)
    else: 
        # Look north on map
        if y > 0:
            if topographic_map[y-1][x] == elev + 1:
                get_trail_score(y-1, x, elev+1, nines)

        # Look south on map
        if y < len(topographic_map) -1:
            if topographic_map[y+1][x] == elev + 1:
                get_trail_score(y+1, x, elev+1, nines)

        # Look east on map
        if x < len(topographic_map[0]) -1:
            if topographic_map[y][x+1] == elev + 1:
                get_trail_score(y, x+1, elev+1, nines)

        # Look west on map
        if x > 0:
            if topographic_map[y][x-1] == elev + 1:
                get_trail_score(y, x-1, elev+1, nines)
        
        return nines


scores = []
for y, x in trailheads:
    scores.append(len(get_trail_score(y, x, 0, set())))


print("part one:", sum(scores))

def get_trail_rating(y, x, elev):
    if elev == 9:
        return 1
    else: 
        scores = 0
        # Look north on map
        if y > 0:
            if topographic_map[y-1][x] == elev + 1:
                scores += get_trail_rating(y-1, x, elev+1)

        # Look south on map
        if y < len(topographic_map) -1:
            if topographic_map[y+1][x] == elev + 1:
                scores += get_trail_rating(y+1, x, elev+1)

        # Look east on map
        if x < len(topographic_map[0]) -1:
            if topographic_map[y][x+1] == elev + 1:
                scores += get_trail_rating(y, x+1, elev+1)

        # Look west on map
        if x > 0:
            if topographic_map[y][x-1] == elev + 1:
                scores += get_trail_rating(y, x-1, elev+1)
        
        return scores


scores = []
for y, x in trailheads:
    scores.append(get_trail_rating(y, x, 0))

print("part two:", sum(scores))