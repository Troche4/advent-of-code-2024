file = open("/Users/trey/advent-of-code-2024/8/input.txt", "r")
import itertools

locations_per_frequency = {}
rows = file.read().split("\n")
for i in range(0, len(rows)):
    for j in range(0, len(rows[0])):
        if rows[i][j] != ".":
            frequency = rows[i][j]
            if frequency in locations_per_frequency:
                locations = locations_per_frequency[frequency]
                locations.append((i, j))
            else:
                locations_per_frequency[frequency] = [(i, j)]


possible_antinodes_1 = set()
for freq in locations_per_frequency.keys():
    antennas = locations_per_frequency[freq]
    combinations = itertools.combinations(antennas, 2)
    for subset in combinations:
        dist_y = subset[0][0] - subset[1][0]
        dist_x = subset[0][1] - subset[1][1]
        anti_one = (subset[0][0] + dist_y), (subset[0][1] + dist_x)
        if (anti_one[0] >= 0 and anti_one[0] <= len(rows)-1 and anti_one[1] >= 0 and anti_one[1] <= len(rows[0])-1):
            possible_antinodes_1.add(anti_one)
        anti_two = (subset[1][0] - dist_y), (subset[1][1] - dist_x)
        if (anti_two[0] >= 0 and anti_two[0] <= len(rows)-1 and anti_two[1] >= 0 and anti_two[1] <= len(rows[0])-1):
            possible_antinodes_1.add(anti_two)

mat_1 = []
for i in range(0, len(rows)):
    row = ""
    for j in range(0, len(rows[0])):
        if (i, j) in possible_antinodes_1:
            row += "#"
        else:
            row += '.'
    mat_1.append(row)

for line in mat_1:
    print(line)

print("part one:", len(possible_antinodes_1))
print()

possible_antinodes_2 = set()
for freq in locations_per_frequency.keys():
    antennas = locations_per_frequency[freq]
    if len(antennas) > 1:
        for (x, y) in antennas:
            possible_antinodes_2.add((x, y))
    combinations = itertools.combinations(antennas, 2)
    for subset in combinations:
        dist_y = subset[0][0] - subset[1][0]
        dist_x = subset[0][1] - subset[1][1]
        anti_one = (subset[0][0] + dist_y), (subset[0][1] + dist_x)
        while (anti_one[0] >= 0 and anti_one[0] <= len(rows)-1 and anti_one[1] >= 0 and anti_one[1] <= len(rows[0])-1):
            possible_antinodes_2.add(anti_one)
            anti_one = (anti_one[0] + dist_y, anti_one[1] + dist_x)
        anti_two = (subset[1][0] - dist_y), (subset[1][1] - dist_x)
        while (anti_two[0] >= 0 and anti_two[0] <= len(rows)-1 and anti_two[1] >= 0 and anti_two[1] <= len(rows[0])-1):
            possible_antinodes_2.add(anti_two)
            anti_two = (anti_two[0] - dist_y, anti_two[1] - dist_x)


mat_2 = []
for i in range(0, len(rows)):
    row = ""
    for j in range(0, len(rows[0])):
        if (i, j) in possible_antinodes_2:
            row += "#"
        else:
            row += '.'
    mat_2.append(row)

for line in mat_2:
    print(line)
            
print("part two:", len(possible_antinodes_2))