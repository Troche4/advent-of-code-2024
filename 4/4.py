import re
file = open("/Users/trey/advent-of-code-2024/4/input.txt", "r")

word_search = file.read()

def check_forwards():
    return len(re.findall("XMAS", word_search))

def check_backwards():
    return len(re.findall("SAMX", word_search))

def check_vertical():
    count = 0
    matrix = word_search.split("\n")
    for i in range(0, len(matrix)-3):
        for j in range(0, len(matrix[0])):
            if (matrix[i][j]) == "X" and matrix[i+1][j] == "M" and matrix[i+2][j] == "A" and matrix[i+3][j] == "S":
                count+=1

    return count

def check_vertical_backwards():
    count = 0
    matrix = word_search.split("\n")
    for i in range(0, len(matrix)-3):
        for j in range(0, len(matrix[0])):
            if (matrix[i][j]) == "S" and matrix[i+1][j] == "A" and matrix[i+2][j] == "M" and matrix[i+3][j] == "X":
                count+=1

    return count

def check_diagonal_northwest_to_southeast():
    count = 0
    matrix = word_search.split("\n")
    for i in range(0, len(matrix)-3):
        for j in range(0, len(matrix[0])-3):
            if (matrix[i][j]) == "X" and matrix[i+1][j+1] == "M" and matrix[i+2][j+2] == "A" and matrix[i+3][j+3] == "S":
                count+=1

    return count

def check_diagonal_southeast_to_northwest():
    count = 0
    matrix = word_search.split("\n")
    for i in range(0, len(matrix)-3):
        for j in range(0, len(matrix[0])-3):
            if (matrix[i][j]) == "S" and matrix[i+1][j+1] == "A" and matrix[i+2][j+2] == "M" and matrix[i+3][j+3] == "X":
                count+=1

    return count


def check_diagonal_northeast_to_southwest():
    count = 0
    matrix = word_search.split("\n")
    for i in range(3, len(matrix)):
        for j in range(0, len(matrix[0])-3):
            if (matrix[i][j]) == "S" and matrix[i-1][j+1] == "A" and matrix[i-2][j+2] == "M" and matrix[i-3][j+3] == "X":
                count+=1

    return count


def check_diagonal_southwest_to_northeast():
    count = 0
    matrix = word_search.split("\n")
    for i in range(3, len(matrix)):
        for j in range(0, len(matrix[0])-3):
            if (matrix[i][j]) == "X" and matrix[i-1][j+1] == "M" and matrix[i-2][j+2] == "A" and matrix[i-3][j+3] == "S":
                count+=1

    return count


xmas_total = check_forwards() + check_backwards() + check_vertical() + check_vertical_backwards() + check_diagonal_northwest_to_southeast() + check_diagonal_southeast_to_northwest() + check_diagonal_northeast_to_southwest() +  check_diagonal_southwest_to_northeast()
print("part one:", xmas_total)

def check_m_on_top():
    count = 0
    matrix = word_search.split("\n")
    for i in range(1, len(matrix)-1):
        for j in range(1, len(matrix[0])-1):
            if (matrix[i][j]) == "A" and matrix[i-1][j-1] == "M" and matrix[i-1][j+1] == "M" and matrix[i+1][j-1] == "S" and matrix[i+1][j+1] == "S":
                count+=1

    return count

def check_m_on_left():
    count = 0
    matrix = word_search.split("\n")
    for i in range(1, len(matrix)-1):
        for j in range(1, len(matrix[0])-1):
            if (matrix[i][j]) == "A" and matrix[i-1][j-1] == "M" and matrix[i-1][j+1] == "S" and matrix[i+1][j-1] == "M" and matrix[i+1][j+1] == "S":
                count+=1

    return count

def check_x_on_right():
    count = 0
    matrix = word_search.split("\n")
    for i in range(1, len(matrix)-1):
        for j in range(1, len(matrix[0])-1):
            if (matrix[i][j]) == "A" and matrix[i-1][j-1] == "S" and matrix[i-1][j+1] == "M" and matrix[i+1][j-1] == "S" and matrix[i+1][j+1] == "M":
                count+=1

    return count

def check_x_on_bottom():
    count = 0
    matrix = word_search.split("\n")
    for i in range(1, len(matrix)-1):
        for j in range(1, len(matrix[0])-1):
            if (matrix[i][j]) == "A" and matrix[i-1][j-1] == "S" and matrix[i-1][j+1] == "S" and matrix[i+1][j-1] == "M" and matrix[i+1][j+1] == "M":
                count+=1

    return count

cross_mas = check_m_on_top() + check_m_on_left() + check_x_on_right() + check_x_on_bottom()
print("part two:", cross_mas)