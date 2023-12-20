import sys

# input = """
# O....#....
# O.OO#....#
# .....##...
# OO.#O....O
# .O.....O#.
# O.#..O.#.#
# ..O..#O..O
# .......O..
# #....###..
# #OO..#....
# """

def process_cell(array, row, col, row_step, col_step):
    if array[row][col] == 'O':
        newRow, newCol = row + row_step, col + col_step
        while 0 <= newRow < len(array) and 0 <= newCol < len(array[0]) and array[newRow][newCol] == '.':
            array[row][col], row, col = '.', newRow, newCol
            newRow, newCol = row + row_step, col + col_step
        array[row][col] = 'O'

with open("input.txt") as f:
    input = f.read()

cycles = 1000000000

# Splitting the string into lines
lines = input.strip().split('\n')
linesAsArray = []

for line in lines:
    innerArray = []
    innerArray = [*line]
    linesAsArray.append(innerArray)

# for line in linesAsArray:
#     print(line)

for cycle in range(cycles):
    percent_complete = float(100 * (cycle / cycles))
    # Creating the bar representation
    bar = '#' * int(percent_complete) + '-' * (100 - int(percent_complete))
    # Writing the bar to the console with the percentage
    sys.stdout.write(f"\r[{bar}] {percent_complete}%")
    sys.stdout.flush()

    numRows, numCols = len(linesAsArray), len(linesAsArray[0])

    for col in range(numCols):
        for row in range(numRows):
            process_cell(linesAsArray, row, col, -1, 0)

    for row in range(numRows):
        for col in range(numCols):
            process_cell(linesAsArray, row, col, 0, -1)


    for col in range(numCols):
        for row in reversed(range(numRows)):
            process_cell(linesAsArray, row, col, 1, 0)

    for row in range(numRows):
        for col in reversed(range(numCols)):
            process_cell(linesAsArray, row, col, 0, 1)

# print('#######')
# for line in linesAsArray:
#      print(line)

lineNum = len(linesAsArray)

overallCount = 0
for line in linesAsArray:
    countInLine = 0
    for char in line:
        if char == 'O':
            countInLine += 1
    overallCount += countInLine*lineNum
    lineNum -= 1


print("Solution is: " + str(overallCount))
