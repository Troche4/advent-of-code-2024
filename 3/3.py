import re
file = open("/Users/trey/advent-of-code-2024/3/input.txt", "r")

mem = file.read()

multiplications = re.findall(r'mul[(]\d{1,3},\d{1,3}[)]', mem)

total = 0
for cmd in multiplications:
    numbers = list(map(int, re.findall(r'\d{1,3}', cmd)))
    total += numbers[0] * numbers[1]

print("part one:", total)

enabled_total = 0
toggle_multiplications = re.findall(r"mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\)", mem)
on = True
for cmd in toggle_multiplications:
    print(cmd)
    print()
    if cmd == "do()":
        on = True
    elif cmd == "don't()":
        on = False
    else:
        if on:
            x, y = map(int, cmd[4:-1].split(","))
            enabled_total += x * y
    
print("part two:", enabled_total)