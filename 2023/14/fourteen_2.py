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

    # north tilt
    for columnNum in range(len(linesAsArray[0])):
        for rowNum in range(len(linesAsArray)):
            #print(lines[rowNum][columnNum])
            currentSign = linesAsArray[rowNum][columnNum]
            if currentSign == 'O':
                setO = False
                newRowNum = rowNum
                while not setO:
                    if newRowNum == 0:
                        setO = True
                    elif linesAsArray[newRowNum - 1][columnNum] == '.':
                        #print('I am at: ' + str(columnNum) + str(rowNum))
                        linesAsArray[newRowNum][columnNum] = '.'
                        newRowNum = newRowNum - 1
                        linesAsArray[newRowNum][columnNum] = 'O'
                    elif linesAsArray[newRowNum - 1][columnNum] == '#' or linesAsArray[newRowNum - 1][columnNum] == 'O':
                        setO = True

    # west tilt
    for rowNum in range(len(linesAsArray)):
        for columnNum in range(len(linesAsArray[0])):
            #print(lines[rowNum][columnNum])
            currentSign = linesAsArray[rowNum][columnNum]
            if currentSign == 'O':
                setO = False
                newColumNum = columnNum
                while not setO:
                    #print('I am at: ' + str(newColumNum) + str(rowNum))
                    if newColumNum == 0:
                        setO = True
                    elif linesAsArray[rowNum][newColumNum-1] == '.':
                        linesAsArray[rowNum][newColumNum] = '.'
                        newColumNum = newColumNum - 1
                        linesAsArray[rowNum][newColumNum] = 'O'
                    elif linesAsArray[rowNum][newColumNum - 1] == '#' or linesAsArray[rowNum][newColumNum - 1] == 'O':
                        setO = True

    # south tilt
    for columnNum in range(len(linesAsArray[0])):
        for x in range(len(linesAsArray)):
            rowNum = len(linesAsArray) - 1 - x
            #print(lines[rowNum][columnNum])
            currentSign = linesAsArray[rowNum][columnNum]
            if currentSign == 'O':
                setO = False
                newRowNum = rowNum
                while not setO:
                    #print('I am at: ' + str(columnNum) + str(newRowNum))
                    if newRowNum == len(linesAsArray)-1:
                        setO = True
                    elif linesAsArray[newRowNum + 1][columnNum] == '.':
                        linesAsArray[newRowNum][columnNum] = '.'
                        newRowNum = newRowNum + 1
                        linesAsArray[newRowNum][columnNum] = 'O'
                    elif linesAsArray[newRowNum + 1][columnNum] == '#' or linesAsArray[newRowNum + 1][columnNum] == 'O':
                        setO = True
                    else:
                        setO = True

    # east tilt
    for rowNum in range(len(linesAsArray)):
        for x in range(len(linesAsArray[0])):
            columnNum = len(linesAsArray[0]) - 1 - x
            #print(lines[rowNum][columnNum])
            currentSign = linesAsArray[rowNum][columnNum]
            if currentSign == 'O':
                setO = False
                newColumNum = columnNum
                while not setO:
                    #print('I am at: ' + str(newColumNum) + str(rowNum))
                    if newColumNum == len(linesAsArray[0]) - 1:
                        setO = True
                    elif linesAsArray[rowNum][newColumNum+1] == '.':
                        linesAsArray[rowNum][newColumNum] = '.'
                        newColumNum = newColumNum + 1
                        linesAsArray[rowNum][newColumNum] = 'O'
                    elif linesAsArray[rowNum][newColumNum + 1] == '#' or linesAsArray[rowNum][newColumNum + 1] == 'O':
                        setO = True

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
