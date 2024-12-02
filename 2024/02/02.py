with open('2024/02/input.txt', 'r') as file:
    content = file.read().splitlines()

count = 0
for i, report in enumerate(content):
    report = report.split(' ')
    isSafe = True
    differences = []
    for j, level in enumerate(report):
        if j > 0:
            difference = int(report[j-1]) - int(level)
            #print('difference: ' + str(difference))
            differences.append(difference)
    #print(differences)
    removesCount = 0
    if len(differences) == (len(report) - 1):
        #print(differences[0])
        if differences[0] > 0:
            #positive zahlen
            for k, one in enumerate(differences):
                if one < 0:
                    isSafe = False
                else:
                    if one < 1 or one > 3:
                        isSafe = False
        else:
            #negative zahlen
            for k, one in enumerate(differences):
                if one > 0:
                    isSafe = False
                else:
                    if one > -1 or one < -3:
                        isSafe = False
    if isSafe:
        #print('safe')
        count += 1

print("safe: " + str(count))
                