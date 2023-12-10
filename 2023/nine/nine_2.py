def getNewValue(valuerows):
    valuerows[len(valuerows)-1].append(0)
    for num in reversed(range(len(valuerows))):
        #print("num:" + str(num))
        if num > 0:
            currentrow = valuerows[num]
            currentrowfirstelement = currentrow[0]
            #print("currentrowfirstelement" + str(currentrowfirstelement))
            lastrow = valuerows[num-1]
            lastrowfirstelement = lastrow[0]
            #print("lastrowfirstelement" + str(lastrowfirstelement))
            newelement = int(lastrowfirstelement)-int(currentrowfirstelement)
            #print(newelement)
            lastrow.insert(0, newelement)
            
            valuerows[num-1] = lastrow
        
                
            #print(newelement)
    return newelement


def getNextRows(currentrow, newarray):
    #print(currentrow)
    secondrow = []
    counter = 0
    for (index, number) in enumerate(currentrow):
        if (index + 1 < len(currentrow)):
            newnumber = int(currentrow[index+1]) - int(number)
            secondrow.append(newnumber)
            if newnumber == 0:
                counter+=1
    newarray.append(secondrow)
    if (counter == len(secondrow)):
        return
    else:
        getNextRows(secondrow, newarray)


inputA = """10 13 16 21 30 45"""

with open("input.txt") as f:
    input = f.read()

lines = input.split('\n')
finalCounter = 0

for (index,line) in enumerate(lines):
    #print(index+1)
    numbers = line.strip().split(' ')
    resultArray = [numbers]
    getNextRows(numbers, resultArray)
    #print(resultArray)
    result = getNewValue(resultArray)
    #print(result)
    finalCounter += result

print("Fianl Result: " + str(finalCounter))
    


