import copy
from tqdm import tqdm

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
counter = 0

def check_if_ive_been_there_and_went_same_direction(position, direction):
    for place in places_ive_been:
        if place[0] == position and place[1] == direction:
            return True
        
def check_if_ive_been_there_and_went_same_direction_or_next_one(position, direction, next_direction):
    for place in places_ive_been:
        if place[0] == position and (place[1] == direction or place[1] == next_direction):
            return True

def go_up(position, places_ive_been, allLines):
    while position[0] != 0 and allLines[position[0] - 1][position[1]] == '.':
        position = (position[0] - 1, position[1])
        if check_if_ive_been_there_and_went_same_direction(position, '^'):
            global counter
            counter += 1
            #print('add 1 (go_up): ' + str(position))
            return None
        places_ive_been.append((position, '^'))
    return position

def go_right(position, places_ive_been, allLines):
    while position[1] != len(allLines[0]) - 1 and allLines[position[0]][position[1] + 1] == '.':
        position = (position[0], position[1] + 1)
        if check_if_ive_been_there_and_went_same_direction(position, '>'):
            global counter
            counter += 1
            #print('add 1 (go_right): ' + str(position))
            return None
        places_ive_been.append((position, '>'))
    return position

def go_down(position, places_ive_been, allLines):
    while position[0] != len(allLines) - 1 and allLines[position[0] + 1][position[1]] == '.':
        position = (position[0] + 1, position[1])
        if check_if_ive_been_there_and_went_same_direction(position, 'v'):
            global counter
            counter += 1
            #print('add 1 (go_down): ' + str(position))
            return None
        places_ive_been.append((position, 'v'))
    return position

def go_left(position, places_ive_been, allLines):
    while position[1] != 0 and allLines[position[0]][position[1] - 1] == '.':
        position = (position[0], position[1] - 1)
        if check_if_ive_been_there_and_went_same_direction(position, '<'):
            global counter
            counter += 1
            #print('add 1 (go_left): ' + str(position))
            return None
        places_ive_been.append((position, '<'))
    return position

def go_around(allLines, position, go_up, go_right, go_down, go_left, places_ive_been):
    maxRounds = 100000
    global counter
# while position doesn't reach end of line, reached end of allLines or reached -1 allLines or -1 line
    while position[1] != (len(allLines[1]) - 1) and position[0] != len(allLines) - 1 and position[0] != 0 and position[1] != 0 and maxRounds > 0:
        if check_if_ive_been_there_and_went_same_direction_or_next_one(position, '^', '>'):
            return True
        position = go_up(position, places_ive_been, allLines)
        #print(str(position) + ' next right')
        if check_if_ive_been_there_and_went_same_direction_or_next_one(position, '>', 'v') or position == None:
            return True
        if position[0] != 0:
            position = go_right(position, places_ive_been, allLines)
            #print(str(position) + ' next down')
            if check_if_ive_been_there_and_went_same_direction_or_next_one(position, 'v', '<') or position == None:
                return True
            if position[1] != len(allLines[1]) - 1:
                position = go_down(position, places_ive_been, allLines)
                #print(str(position) + ' next left')
                if check_if_ive_been_there_and_went_same_direction_or_next_one(position, '<', '^') or position == None:
                    return True
                if position[0] != len(allLines) - 1:
                    position = go_left(position, places_ive_been, allLines)
                    #print(str(position) + ' next up')
                    if position == None:
                        return True
        maxRounds -= 1

obstacles = []
for x, line in enumerate(tqdm(allLines, desc="Processing lines")):
#for x, line in enumerate(allLines):
    for y, char in enumerate(tqdm(line, desc="Processing characters", leave=False)):
    #for y, char in enumerate(line):
        oldcounter = copy.deepcopy(counter)
        copyOfAllLines = []
        copyOfAllLines = copy.deepcopy(allLines)
        if char == '.':
            copyOfAllLines[x][y] = '#'
            position = (x, y)
            places_ive_been = []
            if go_around(copyOfAllLines, firstPosition, go_up, go_right, go_down, go_left, places_ive_been):
                obstacles.append((x, y))
        # # replace all places_ive_been with 'O' in allLines
        # for place in places_ive_been:
        #     copyOfAllLines[place[0][0]][place[0][1]] = 'O'
        # # write allLines to output.txt
        # with open('2024/06/output' + str(x) + str(y) + '.txt', 'w') as file:
        #     for line in copyOfAllLines:
        #         file.write(''.join(line) + '\n')
        # # if counter increased by 1 print x, y
        # if counter > oldcounter:
        #     print('x: ' + str(x) + ' y: ' + str(y) + ' counter: ' + str(counter))
        

# print(counter)
print(obstacles)
print(len(obstacles))

