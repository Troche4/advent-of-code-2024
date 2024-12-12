file = open("/Users/trey/advent-of-code-2024/12/input.txt", "r")

def avg(x, y):
    return (x + y) / 2

# Represent file as 2D matrix
rows = file.read().split("\n")
map = []
for row in rows:
    map_row = []
    for plot in row:
        map_row.append(plot)
    map.append(map_row)

# list of dictionaries with keys for plant and coordinates
regions = []
for i in range(0, len(map)):
    for j in range(0, len(map[0])):
        plant = map[i][j]
        existing_regions = [r for r in regions if r["plant"] == plant]
        if len(existing_regions) == 0:
            regions.append({"plant": plant, "coordinates": [[i,j]]})
        else:
            found_match = False
            for r in range(0, len(existing_regions)):
                region = existing_regions[r]
                for pair in region["coordinates"]:
                    if (abs(pair[0] - i) == 1 or abs(pair[1] - j) == 1) and not found_match:
                        region["coordinates"].append([i,j])
                        found_match = True
            if not found_match:
                regions.append({"plant": plant, "coordinates": [[i,j]]})

perimeters = []
areas = []
for r in range(0, len(regions)):
    distinct_fences = set()
    coordinates = regions[r]["coordinates"]
    for i, j in coordinates:
        plant = map[i][j]
        if i > 0 and map[i-1][j] != plant:
            distinct_fences.add((avg(i, i-1), j))
        if i < len(map) - 1 and map[i+1][j] != plant:
            distinct_fences.add((avg(i, i+1), j))
        if j > 0 and map[i][j-1] != plant:
            distinct_fences.add((i, avg(j, j-1)))
        if j < len(map) - 1 and map[i][j+1] != plant:
            distinct_fences.add((i, avg(j, j+1)))
    regions[r]["perimeter"] = len(distinct_fences)
    regions[r]["area"] = len(regions[r]["coordinates"])

for r in regions:
    print("region with plant", r["plant"], "has area", r["area"], "and perimeter", r["perimeter"])


# calculate perimeters by iterating through each plant and checking its neighbors, and adding coordinates for plants that don't match
internal_fences = set()
for i in range(0, len(map)):
    for j in range(0, len(map[0])):
        plant = map[i][j]
        if i > 0 and map[i-1][j] != plant:
            internal_fences.add((avg(i, i-1), j))
        if i < len(map) - 1 and map[i+1][j] != plant:
            internal_fences.add((avg(i, i+1), j))
        if j > 0 and map[i][j-1] != plant:
            internal_fences.add((i, avg(j, j-1)))
        if j < len(map) - 1 and map[i][j+1] != plant:
            internal_fences.add((i, avg(j, j+1)))

total_perimeter = (2 * (len(map) + len(map[0]))) + len(internal_fences)

print("part one:", 0)

print("part two:", 0)