import re
file = open("/Users/trey/advent-of-code-2024/5/input.txt", "r")

lines = file.read().split("\n\n")
rules = lines[0].split("\n")
updates = lines[1].split("\n")

x_must_come_before = {}
for x in range(0, 100):
    x_must_come_before[x] = []

for rule in rules:
    before, after = list(map(int, rule.split("|")))

    before_list = x_must_come_before[before]
    before_list.append(after)
    x_must_come_before[before] = before_list

middle_page_numbers = []
invalid_instructions = []
for instruction in updates:
    invalid = False
    page_numbers = list(map(int, instruction.split(",")))
    updates_done = list()
    for update in page_numbers:
        updates_done.append(update)
        numbers_cannot_be_printed_yet = x_must_come_before[update]
        for prohibited in numbers_cannot_be_printed_yet:
            if prohibited in updates_done:
                invalid = True

    index = len(page_numbers) // 2
    if not invalid:
        middle_page_numbers.append(page_numbers[index])
    else:
        invalid_instructions.append(page_numbers[index])

print("part one:", sum(middle_page_numbers))
print("part two:", sum(invalid_instructions))