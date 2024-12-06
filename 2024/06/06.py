with open('2024/06/input.txt', 'r') as file:
    lines = file.read().splitlines()

# create a list of all lines and chars in lines
allLines = []
for line in lines:
    allLines.append(list(line))

# find the position of '^' in allLines
for i, line in enumerate(allLines):
    for j, char in enumerate(line):
        if char == '^':
            position = (i, j)
            firstPosition = position
            allLines[i][j] = '.'
            break

places_ive_been = []

def go_up(position):
    while position[0] != 0 and allLines[position[0] - 1][position[1]] == '.':
        position = (position[0] - 1, position[1])
        places_ive_been.append(position)
    return position

def go_right(position):
    while position[1] != len(allLines[0]) - 1 and allLines[position[0]][position[1] + 1] == '.':
        position = (position[0], position[1] + 1)
        places_ive_been.append(position)
    return position

def go_down(position):
    while position[0] != len(allLines) - 1 and allLines[position[0] + 1][position[1]] == '.':
        position = (position[0] + 1, position[1])
        places_ive_been.append(position)
    return position

def go_left(position):
    while position[1] != 0 and allLines[position[0]][position[1] - 1] == '.':
        position = (position[0], position[1] - 1)
        places_ive_been.append(position)
    return position

maxRounds = 150
# while position doesn't reach end of line, reached end of allLines or reached -1 allLines or -1 line
while position[1] != (len(allLines[1]) - 1) and position[0] != len(allLines) - 1 and position[0] != 0 and position[1] != 0 and maxRounds > 0:
    position = go_up(position)
    print(str(position) + ' next right')
    if position[0] != 0:
        position = go_right(position)
        print(str(position) + ' next down')
        if position[1] != len(allLines[1]) - 1:
            position = go_down(position)
            print(str(position) + ' next left')
            if position[0] != len(allLines) - 1:
                position = go_left(position)
                print(str(position) + ' next up')
    maxRounds -= 1

print(len(allLines[0]))
# make all places_ive_been unique
places_ive_been = list(set(places_ive_been))

# count all places_ive_been
count = len(places_ive_been)
print(count+1)

# replace all places_ive_been with 'O' in allLines
for place in places_ive_been:
    allLines[place[0]][place[1]] = 'O'

allLines[firstPosition[0]][firstPosition[1]] = 'X'
allLines[23][129] = 'Y'

# write allLines to output.txt
with open('2024/06/output.txt', 'w') as file:
    for line in allLines:
        file.write(''.join(line) + '\n')

#5019 too high
#4976