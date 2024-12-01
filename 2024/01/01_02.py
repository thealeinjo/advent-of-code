

# open input.txt and ready file content
firstList = []
secondList = []
with open('01/input.txt', 'r') as file:
    content = file.read().splitlines()
    for count, i in enumerate(content):
        splitContent = content[count].split('   ')
        firstList.append(splitContent[0])
        secondList.append(splitContent[1])

sum = 0
for count, i in enumerate(firstList):
    multiplier = secondList.count(i)
    multiple = int(i) * multiplier
    sum += multiple

print(sum)
