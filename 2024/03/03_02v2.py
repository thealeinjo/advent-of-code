import re

dontPattern = r'don\'t\(\)'
pattern = r'mul\(\d+,\d+\)'
doPattern2 = r'do\(\)(?:(?!don\'t\(\)).)*?mul\(\d+,\d+\)'
firstPattern = r'(?:(?!don\'t\(\)).)*?mul\(\d+,\d+\)'

with open('2024/03/input_x.txt', 'r') as file:
    lines = file.read().splitlines()

sum = 0

for line in lines:
    # Find the first part that matches the pattern without don't()
    firstLine = re.split(pattern, line)
    print('firstLine)' + str(firstLine))
    #firstPart = re.findall(firstPattern, line)
    #print('firstPart)' + str(firstPart))
    #if firstPart:
    if "don't" not in firstLine[0]:
        matchFirst = re.findall(pattern, firstLine[1])
        if matchFirst:
            match = matchFirst[0].split('(')[1].split(')')[0].split(',')
            multiple = int(match[0]) * int(match[1])
            sum += multiple

    # Find matches for do() followed by mul(*,*) without don't() in between
    matchesDo = re.findall(doPattern2, line)
    print(matchesDo)

    for matchDo in matchesDo:
        matchDo = re.findall(pattern, matchDo)
        if matchDo:
            match = matchDo[0].split('(')[1].split(')')[0].split(',')
            print(match)
            multiple = int(match[0]) * int(match[1])
            sum += multiple

print(sum)


# sum = 0
# for content in lines:
#     split = re.split(pattern, content)
#     matches = re.findall(pattern, content)
#     for i, match in enumerate(matches):
#         #print(matches)

#         donts = list(re.finditer(dontPatter, split[i]))
#         dos = list(re.finditer(doPattern, split[i]))

#         #print(split[i])
#         #print(get_last_non_null(donts))
#         #print(get_last_non_null(dos))
#         #print(len(dos))

#         if get_last_non_null(donts) != None and get_last_non_null(dos) != None:
#             if(get_last_non_null(donts) < get_last_non_null(dos)):
#                 answer = True
#             else:
#                 answer = False
#         elif get_last_non_null(donts) != None:
#             answer = False
#         elif get_last_non_null(dos) != None:
#             answer = True
#         elif i == 0:
#             answer = True
#         else:
#             answer = False

#         #print(answer)

#         #print(split[i])
#         # if re.search(dontPatter, split[i]):
#         #     print(split[i])
#         #     answer = False
#         # else:
#         #     answer = True

#         if answer:
#             match = match.split('(')[1].split(')')[0].split(',')
#             multiple = int(match[0]) * int(match[1])
#             #print(multiple)
#             sum += multiple

# print(sum)

#10772719 + 268,621(166428) =10939147

#12678538

#13706515

13706515