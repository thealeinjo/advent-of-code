import re

def get_last_non_null(array):
    for item in reversed(array):
        if item is not None:
            return item.start()
    return None

with open('2024/03/input_x.txt', 'r') as file:
    lines = file.read().splitlines()

pattern = r'mul\(\d+,\d+\)'
doPattern = r'do\(\)'
dontPatter = r'don\'t\(\)'

sum = 0
for content in lines:
    split = re.split(pattern, content)
    matches = re.findall(pattern, content)
    for i, match in enumerate(matches):
        #print(matches)

        donts = list(re.finditer(dontPatter, split[i]))
        dos = list(re.finditer(doPattern, split[i]))

        #print(split[i])
        #print(get_last_non_null(donts))
        #print(get_last_non_null(dos))
        #print(len(dos))

        if get_last_non_null(donts) != None and get_last_non_null(dos) != None:
            if(get_last_non_null(donts) < get_last_non_null(dos)):
                answer = True
            else:
                answer = False
        elif get_last_non_null(donts) != None:
            answer = False
        elif get_last_non_null(dos) != None:
            answer = True
        elif i == 0:
            answer = True
        else:
            answer = False

        #print(answer)

        #print(split[i])
        # if re.search(dontPatter, split[i]):
        #     print(split[i])
        #     answer = False
        # else:
        #     answer = True

        if answer:
            match = match.split('(')[1].split(')')[0].split(',')
            multiple = int(match[0]) * int(match[1])
            #print(multiple)
            sum += multiple

print(sum)

#10772719 + 268,621(166428) =10939147

#12678538

#13706515

#122730190
#109663031
#100189366