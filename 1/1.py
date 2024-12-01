file = open("/Users/trey/advent-of-code-2024/1/input.txt", "r")

leftInputList = []
rightInputList = []

for line in file.read().split("\n"):
    ids = line.split("   ")
    leftInputList.append(int(ids[0]))
    rightInputList.append(int(ids[1]))
    
leftInputList.sort()
rightInputList.sort()

totalDistances = []
for i in range(0, len(leftInputList)):
    left = leftInputList[i]
    right = rightInputList[i]
    totalDistances.append(abs(right - left))


print("part one:", sum(totalDistances))

similarityScores = []
for i in range(0, len(leftInputList)):
    left = leftInputList[i]
    occurrences = rightInputList.count(left)
    similarityScores.append(left * occurrences)

print("part two:", sum(similarityScores))

