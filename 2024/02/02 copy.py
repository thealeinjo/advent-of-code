def getDifferences(newreport):
    differences = []
    for j, level in enumerate(newreport):
        if j > 0:
            difference = int(newreport[j-1]) - int(level)
            differences.append(difference)
    return differences

def checkDifferences(differences):
    if differences[0] > 0:
        #positive zahlen
        for k, one in enumerate(differences):
            if one < 0:
                return False
            else:
                if one < 1 or one > 3:
                    return False
    else:
        #negative zahlen
        for k, one in enumerate(differences):
            if one > 0:
                return False
            else:
                if one > -1 or one < -3:
                    return False
    return True

def checkDifferencesAndRemove(report):
    removesCount = 1
    if differences[0] > 0:
        #positive zahlen
        for k, one in enumerate(differences):
            if one < 0:
                if removesCount == 1:
                    removesCount = 0
                    report.pop(k)
            else:
                if one < 1 or one > 3:
                    if removesCount == 1:
                        removesCount = 0
                        report.pop(k)
    else:
        #negative zahlen
        for k, one in enumerate(differences):
            if one > 0:
                if removesCount == 1:
                    removesCount = 0
                    report.pop(k)
            else:
                if one > -1 or one < -3:
                    if removesCount == 1:
                        removesCount = 0
                        report.pop(k)
    return report

def checkDifferencesAndRemoveSecond(oldReport):
    removesCount = 1
    if differences[0] > 0:
        #positive zahlen
        for k, one in enumerate(differences):
            if one < 0:
                if removesCount == 1:
                    removesCount = 0
                    oldReport.pop(k+1)
            else:
                if one < 1 or one > 3:
                    if removesCount == 1:
                        removesCount = 0
                        oldReport.pop(k+1)
    else:
        #negative zahlen
        for k, one in enumerate(differences):
            if one > 0:
                if removesCount == 1:
                    removesCount = 0
                    oldReport.pop(k+1)
            else:
                if one > -1 or one < -3:
                    if removesCount == 1:
                        removesCount = 0
                        oldReport.pop(k+1)
    return oldReport

with open('2024/02/input.txt', 'r') as file:
    content = file.read().splitlines()

count = 0
for i, report in enumerate(content):
    report = report.split(' ')
    oldReport = report.copy()
    #print('report1: ' + str(report))
    isSafe = True
    differences = getDifferences(report)
    #print(differences)
    removesCount = 0
    #print(differences)
    isSafe = checkDifferences(differences)


    workingReport = oldReport.copy()
    for i, number in enumerate(workingReport):
            anotherCopy = workingReport.copy()
            anotherCopy.pop(i)
            differences = getDifferences(anotherCopy)
            isSafe = checkDifferences(differences)
            if isSafe:
                break
    # if isSafe == False:
    #     newreport = checkDifferencesAndRemove(report)
        
    #     newDifference = getDifferences(newreport)
    #     #print('differences: ' + str(newDifference))
    #     isSafe = checkDifferences(newDifference)
    #     if isSafe == False:
    #         print('oldreport: ' + str(oldReport))
    #         newreport = checkDifferencesAndRemoveSecond(oldReport)
    #         print('newreport: ' + str(report))
    #         newDifference = getDifferences(newreport)
    #         print('differences: ' + str(newDifference))
    #         isSafe = checkDifferences(newDifference)
        
    if isSafe:
        #print('safe')
        count += 1

print("safe: " + str(count))
                