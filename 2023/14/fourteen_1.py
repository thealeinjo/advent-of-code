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

# Splitting the string into lines
lines = input.strip().split('\n')
linesAsArray = []

for line in lines:
    innerArray = []
    innerArray = [*line]
    linesAsArray.append(innerArray)

# for line in linesAsArray:
#     print(line)

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

#print('#######')
# for line in linesAsArray:
#     print(line)

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
