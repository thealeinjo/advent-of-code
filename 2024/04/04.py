import re

with open('2024/04/input.txt', 'r') as file:
    lines = file.read().splitlines()

patternNormal = r'XMAS'
patternBackwards = r'SAMX'
count = 0

def count_matches_in_line(patternNormal, patternBackwards, count, line):
    matches = re.findall(patternNormal, line)
    matches += re.findall(patternBackwards, line)
    #print(match)
    for match in matches:
        count += 1
    return count

for line in lines:
    count = count_matches_in_line(patternNormal, patternBackwards, count, line)

print('horizontal count: '+str(count))

pivoted_array = list(map(list, zip(*lines)))

for line in pivoted_array:
    count = count_matches_in_line(patternNormal, patternBackwards, count, ''.join(line))

print('+vertical count= ' + str(count))

# diagonal count
#for i in range(0, len(lines)):
#    count = count_matches_in_line(patternNormal, patternBackwards, count, ''.join([line[i] for line in lines]))

for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char == 'X':
            # v >
            if len(lines) > i+3 and len(lines[i]) > j+3:
                if lines[i+1][j+1] == 'M' and lines[i+2][j+2] == 'A' and lines[i+3][j+3] == 'S':
                    count += 1
            # v <
            if len(lines) > i+3 and j-3 >= 0:
                if lines[i+1][j-1] == 'M' and lines[i+2][j-2] == 'A' and lines[i+3][j-3] == 'S':
                    count += 1
            # ^ >
            if i-3 >= 0 and len(lines[i]) > j+3:
                if lines[i-1][j+1] == 'M' and lines[i-2][j+2] == 'A' and lines[i-3][j+3] == 'S':
                    count += 1
            # ^ <
            if i-3 >= 0 and j-3 >= 0:
                if lines[i-1][j-1] == 'M' and lines[i-2][j-2] == 'A' and lines[i-3][j-3] == 'S':
                    count += 1


print('+diagonal count= '+str(count))

# first try: 2529 too high
# 1670 too low
#2521