def get_middle_number(array):
    length = len(array)
    if length == 0:
        return None  # Handle empty array case
    middle_index = length // 2
    return array[middle_index]

def order_correctly(array):
    notCorrectYet = True
    while notCorrectYet:
        notCorrectYet = False
        for i, number in enumerate(array):
            filtered_array = [i for i in arrayRules if i[0] == number]
            #print(str(number) + ' ' + str(filtered_array))
            # check all numbers before this number and check if they are in the filtered_array on the second position
            for j in range(0, i):
                #print('checking ' + str(numbers[j]))
                filtered_array2 = [i for i in filtered_array if i[1] == array[j]]
                #print('filtered_array ' + str(filtered_array2))
                for k in filtered_array2:
                    if k[0] == number:
                        #print('found a problem' + str(k))
                        #print('Problem in Line: ' + str(linenumber) + ' with number ' + str(number) + ' and ' + str(line[j]))
                        #move number from position i to position j
                        array[i], array[j] = array[j], array[i]
                        notCorrectYet = True
                        #break
    return array

with open('2024/05/input.txt', 'r') as file:
    parts = file.read().split('\n\n')

# parts[0] is the rules
# parts[1] is the order
lines = parts[0].splitlines()
arrayRules = []
for line in lines:
    arrayRules.append(line.split('|'))

lines = parts[1].splitlines()
arrayOrders = []
for line in lines:
    arrayOrders.append(line.split(','))

allLines = arrayOrders.copy()
wrongLineNumbers = []

#print(arrayOrders)
for linenumber, line in enumerate(arrayOrders):
    for i, number in enumerate(line):
        filtered_array = [i for i in arrayRules if i[0] == number]
        #print(str(number) + ' ' + str(filtered_array))
        # check all numbers before this number and check if they are in the filtered_array on the second position
        for j in range(0, i):
            #print('checking ' + str(numbers[j]))
            filtered_array2 = [i for i in filtered_array if i[1] == line[j]]
            #print('filtered_array ' + str(filtered_array2))
            for k in filtered_array2:
                if k[0] == number:
                    #print('found a problem' + str(k))
                    #print('Problem in Line: ' + str(linenumber) + ' with number ' + str(number) + ' and ' + str(line[j]))
                    wrongLineNumbers.append(linenumber)
                    break

# if allLines index not in wronglinenumbers write 'right' into the array
for i, line in enumerate(allLines):
    if i not in wrongLineNumbers:
        allLines[i] = 'RIGHT'

allIncorrectLines = [i for i in allLines if i != 'RIGHT']

orderedLines = []

for i in allIncorrectLines:
    neworder = order_correctly(i)
    print(neworder)
    orderedLines.append(neworder)

count = 0
for i in orderedLines:
    count += int(get_middle_number(i))

print('sum: ' + str(count))

