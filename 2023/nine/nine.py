def getNewValue(valuerows):
    valuerows[len(valuerows)-1].append(0)
    for num in reversed(range(len(valuerows))): 
        currentrow = valuerows[num]
        currentrowlastelement = currentrow[len(currentrow)-1]
        #print("currentrowlastelement" + str(currentrowlastelement))
        lastrow = valuerows[num-1]
        lastrowlastelement = lastrow[len(lastrow)-1]
        #print("lastrowlastelement" + str(lastrowlastelement))
        newelement = int(currentrowlastelement)+int(lastrowlastelement)
        lastrow.append(newelement)
        
        valuerows[num-1] = lastrow
    
            
        #print(newelement)
    return newelement


def getNextRows(currentrow, newarray):
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


inputEx = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""

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
    


