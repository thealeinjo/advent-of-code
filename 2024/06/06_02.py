with open('2024/06/input_x.txt', 'r') as file:
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

places_ive_been = [(firstPosition, '^')]

newcount = 0
othercount = 0

def check_if_ive_been_there_and_went_right(position, direction):
    for place in places_ive_been:
        if place[0] == position and place[1] == direction:
            print(place)
            global newcount
            newcount += 1
            print('new obstacle =' + str(position))
            return True

def go_up(position):
    while position[0] != 0 and allLines[position[0] - 1][position[1]] == '.':
        position = (position[0] - 1, position[1])
        if check_if_ive_been_there_and_went_right(position, '^'):
            global othercount
            othercount += 1
            return None
        places_ive_been.append((position, '^'))
    return position

def go_right(position):
    while position[1] != len(allLines[0]) - 1 and allLines[position[0]][position[1] + 1] == '.':
        position = (position[0], position[1] + 1)
        if check_if_ive_been_there_and_went_right(position, '>'):
            global othercount
            othercount += 1
            return None
        places_ive_been.append((position, '>'))
    return position

def go_down(position):
    while position[0] != len(allLines) - 1 and allLines[position[0] + 1][position[1]] == '.':
        position = (position[0] + 1, position[1])
        if check_if_ive_been_there_and_went_right(position, 'v'):
            global othercount
            othercount += 1
            return None
        places_ive_been.append((position, 'v'))
    return position

def go_left(position):
    while position[1] != 0 and allLines[position[0]][position[1] - 1] == '.':
        position = (position[0], position[1] - 1)
        if check_if_ive_been_there_and_went_right(position, '<'):
            global othercount
            othercount += 1
            return None
        places_ive_been.append((position, '<'))
    return position

def go_around(allLines, position, go_up, go_right, go_down, go_left):
    maxRounds = 150
# while position doesn't reach end of line, reached end of allLines or reached -1 allLines or -1 line
    while position[1] != (len(allLines[1]) - 1) and position[0] != len(allLines) - 1 and position[0] != 0 and position[1] != 0 and maxRounds > 0:
        position = go_up(position)
        if position == None:
            break
    #print(str(position) + ' next right')
        if position[0] != 0:
            position = go_right(position)
            if position == None:
                break
        #print(str(position) + ' next down')
            if position[1] != len(allLines[1]) - 1:
                position = go_down(position)
                if position == None:
                    break
            #print(str(position) + ' next left')
                if position[0] != len(allLines) - 1:
                    position = go_left(position)
                    if position == None:
                        break
                #print(str(position) + ' next up')
        maxRounds -= 1

for y, line in enumerate(allLines):
    for x, char in enumerate(line):
        new_grid = []
        new_grid = allLines.copy()
        #print(new_grid)
        new_grid[y][x] = '#'
        go_around(new_grid, position, go_up, go_right, go_down, go_left)

#print(len(allLines[0]))
print(othercount)

# replace all places_ive_been with 'O' in allLines
for place in places_ive_been:
    allLines[place[0][0]][place[0][1]] = place[1]

allLines[firstPosition[0]][firstPosition[1]] = 'X'
#allLines[23][129] = 'Y'

# write allLines to output.txt
with open('2024/06/output.txt', 'w') as file:
    for line in allLines:
        file.write(''.join(line) + '\n')

#5019 too high
#4977

#936 too low