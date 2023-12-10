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

counterDir = 0
counter = 0
#nextstep = lines[startingindex][0]
#currentIdex = findNextPlace(nextstep)[0]
allcurrentsteps = []

for startingindex in startingIndices:
    allcurrentsteps.append(lines[startingindex][0])

print(allcurrentsteps)

while checkAllForZFalse(allcurrentsteps): #and (counter <= 20):
    allcurrentsteps = []
    for index, currentIndex in enumerate(startingIndices):
        #0, 0
        if directions[counterDir] == 'L':
            nextstep = lines[currentIndex][2]
        else:
            nextstep = lines[currentIndex][3]
        #if nextstep[2] == 'Z':
        #    print(nextstep)
        allcurrentsteps.append(nextstep)
        currentIndex = findNextPlace(nextstep)[0]
        startingIndices[index] = currentIndex
    if (counterDir+1 < len(directions)):
        counterDir += 1
    else:
        counterDir = 0
    counter += 1
    #print(allcurrentsteps)
    

print('Result is: ' + str(counter))