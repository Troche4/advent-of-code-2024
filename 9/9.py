file = open("/Users/trey/advent-of-code-2024/9/input.txt", "r")
import re


# Consists of tuples of the size and ID
files = []
free_space = []
input = file.read()
for i in range(0, len(input)):
    if i % 2 == 0:
        files.append((int(input[i]), i//2))
    else:
        free_space.append(int(input[i]))

# Visualize the memory into a list of strings
memory = []
for i in range(0, min(len(files), len(free_space))):
    memory.extend(files[i][0] * [str(files[i][1])])
    memory.extend(free_space[i] * ["."])

if len(files) > len(free_space):
    memory.extend(files[-1][0] * [str(files[-1][1])])
elif len(files) < len(free_space):
    memory.extend(free_space[-1][0] * ["."])

# Replace the free space with files at the end of memory
count = memory.count(".")
for i in range(len(memory) -1, len(memory) - (count + 1), -1):
    if memory[i] != ".":
        insert_index = memory.index(".")
        memory[insert_index] = memory[i]
        memory[i] = "."


# Do checksum
stringified_memory = "".join(memory)
checksum = 0
for i in range(0, len(memory)):
    if memory[i] != ".":
        checksum += (i * int(memory[i]))

print("part one:", checksum)


# Visualize the memory into a list of strings
memory = []
for i in range(0, min(len(files), len(free_space))):
    memory.append(files[i][0] * [str(files[i][1])])
    memory.append(free_space[i] * ["."])

if len(files) > len(free_space):
    memory.append(files[-1][0] * [str(files[-1][1])])
elif len(files) < len(free_space):
    memory.append(free_space[-1][0] * ["."])

memory = [x for x in memory if x != []]

# Replace the free space with files at the end of memory
for i in range(len(memory) -1, -1, -1):
    space_required = len(memory[i])
    if "." not in memory[i]:
        # find first one with at least the proper amount of dots
        for j in range(0, len(memory)):
            if len(memory[j]) == space_required and "." in memory[j]:
                dots = memory[j]
                memory[j] = memory[i]
                memory[i] = dots
            elif len(memory[j]) > space_required and "." in memory[j]:
                dots_needed = len(memory[j]) - len(memory[i])
                dots = memory[j]
                numbers = memory[i]
                for i in range(0, dots_needed):
                    numbers.append(".")
                memory[j] = numbers
                memory[i] = dots


# Do checksum
stringified_memory = ""
for chunk in memory:
    stringified_memory += "".join(chunk)

checksum = 0
for i in range(0, len(memory)):
    if memory[i] != ".":
        checksum += 0

print("part two:", checksum)