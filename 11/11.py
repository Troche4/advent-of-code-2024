file = open("/Users/trey/advent-of-code-2024/11/input.txt", "r")
import functools

input = list(map(int, file.read().split(" ")))

def blink(stones):
    new_stones = []
    for i in range(0, len(stones)):
        engraving = stones[i]
        if engraving == 0:
            new_stones.append(1)
        elif len(str(engraving)) % 2 == 0:
            string_engraving = str(engraving)
            left_half = string_engraving[:len(string_engraving)//2]
            new_stones.append(int(left_half))
            right_half = string_engraving[len(string_engraving)//2:]
            new_stones.append(int(right_half))
        else:
            new_stones.append(2024 * engraving)
    return new_stones

stones_1 = input
for i in range(0, 25):
    stones_1 = blink(stones_1)

print("part one:", len(stones_1))

@functools.cache
def counts_for_stone(engraving, blinks):
    if blinks == 75:
        return 1
    if engraving == 0:
        return counts_for_stone(1, blinks + 1)
    if len(str(engraving)) % 2 == 0:
        string_engraving = str(engraving)
        left_half = int(string_engraving[:len(string_engraving)//2])
        right_half = int(string_engraving[len(string_engraving)//2:])
        return counts_for_stone(left_half, blinks + 1) + counts_for_stone(right_half, blinks + 1)
    return counts_for_stone(engraving * 2024, blinks + 1)

print("part two:", sum(counts_for_stone(x, 0) for x in input))