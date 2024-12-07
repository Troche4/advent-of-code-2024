import re
file = open("/Users/trey/advent-of-code-2024/7/input.txt", "r")
from itertools import product

rows = file.read().split("\n")

part_one_total = 0
for row in rows:
    split_row = row.split(": ")
    expected = int(split_row[0])
    numbers = list(map(int, split_row[1].split(" ")))
    perms = product(["+", "*"], repeat=len(numbers)-1)
    solutions = []
    for perm in perms:
        expr = "(" * len(perm)
        expr += str(numbers[0])
        for i in range(0, len(perm)):
            expr += perm[i]
            expr += str(numbers[i+1])
            expr += ")"

        if eval(expr) == expected:
            solutions.append(expr)
                
    if solutions != []:
        part_one_total += expected
    
print("part one:", part_one_total)



part_two_total = 0
for row in rows:
    split_row = row.split(": ")
    expected = int(split_row[0])
    numbers = list(map(int, split_row[1].split(" ")))
    perms = product(["+", "*", "||"], repeat=len(numbers)-1)
    solutions = []
    for perm in perms:
        expr = "(" * len(perm)
        expr += str(numbers[0])
        for i in range(0, len(perm)):
            expr += perm[i]
            expr += str(numbers[i+1])
            expr += ")"

        if "||" not in expr:
            if eval(expr) == expected:
                solutions.append(expr)
        else:
            custom_eval = 0
            decoded_expr = expr.replace("(", "")
            expr_parts = list(filter(bool, decoded_expr.split(")")))
            for step in expr_parts:
                if "||" in step:
                    custom_eval = int(str(custom_eval) + step.replace("||", ""))
                else:
                    if custom_eval == 0:
                        custom_eval = eval(step)
                    else:
                        step = str(custom_eval) + step
                        custom_eval = eval(step)
            if int(custom_eval) == expected:
                solutions.append(expr)
    
    if solutions != []:
        part_two_total += expected

print("part two:", part_two_total)