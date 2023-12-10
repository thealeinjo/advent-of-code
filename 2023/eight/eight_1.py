def prepareData():
    with open("input.txt") as f:
        input = f.read()

    lines = input.split('\n')

    directions = lines[0]

    lines = lines[2:]

    for index, line in enumerate(lines):
        line = line.replace('=', '')
        line = line.replace('(', '')
        line = line.replace(')', '')
        line = line.replace(',', '')
        line = line.split(' ')
        lines[index] = line

    return directions, lines


def findNextPlace(nextplace):
    return [index for index, array in enumerate(lines) if array[0] == nextplace] 

directions, lines = prepareData()

print(lines)

counterDir = 0
counter = 0

nextstep = 'AAA'
currentIdex = findNextPlace(nextstep)[0]

while nextstep != 'ZZZ':
    if directions[counterDir] == 'L':
        nextstep = lines[currentIdex][2]
    else:
        nextstep = lines[currentIdex][3]
    print(nextstep)
    currentIdex = findNextPlace(nextstep)[0]
    print(counterDir)
    if (counterDir+1 < len(directions)):
        counterDir += 1
    else:
        counterDir = 0
    counter += 1

print('Result is: ' + str(counter))