from math import lcm
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

def findAllA():
    return [index for index, array in enumerate(lines) if array[0][2] == 'A'] 

def checkAllForZFalse(currents):
    counterZ = 0
    for current in currents:
        if (current[2] == 'Z'):
            counterZ+=1
    #print('counterZ: ' + str(counterZ) + str(len(currents)))
    if counterZ == len(currents):
        return False
    else:
        return True

directions, lines = prepareData()

#print(lines)

counters = []

startingIndices = findAllA()
print(startingIndices)

counters = []
#nextstep = lines[startingindex][0]
#currentIdex = findNextPlace(nextstep)[0]
allcurrentsteps = []

for startingindex in startingIndices:
    allcurrentsteps.append(lines[startingindex][0])

print(allcurrentsteps)

for index, currentIndex in enumerate(startingIndices):
    counter = 0
    counterDir = 0
    nextstep = lines[currentIndex][0]
    while (nextstep[2] != 'Z'):
        if directions[counterDir] == 'L':
            nextstep = lines[currentIndex][2]
        else:
            nextstep = lines[currentIndex][3]
        currentIndex = findNextPlace(nextstep)[0]
        if (counterDir+1 < len(directions)):
            counterDir += 1
        else:
            counterDir = 0
        counter += 1
    counters.append(counter)


    #print(allcurrentsteps)
    
print(lcm(counters[0], counters[1], counters[2], counters[3], counters[4], counters[5]))

#print('Result is: ' + str(lcm(counters)))