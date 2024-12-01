

# open input.txt and ready file content
firstList = []
secondList = []
sumList = []
with open('01/input_x.txt', 'r') as file:
    content = file.read().splitlines()
    for count, i in enumerate(content):
        splitContent = content[count].split('   ')
        firstList.append(splitContent[0])
        secondList.append(splitContent[1])



firstList.sort()
secondList.sort()

for count, i in enumerate(firstList):
    sumList.append(int(i) - int(secondList[count]))
    if sumList[count] < 0:
        sumList[count] = sumList[count] * -1

print(sumList)

# add all numbers in sumList
sum = 0
for i in sumList:
    sum += i

print(sum)