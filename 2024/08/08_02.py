import string

# search for a character in a two dimensinal list and return all its positions
def find_char(char, list_of_lists):
    positions = []
    for i, line in enumerate(list_of_lists):
        for j, element in enumerate(line):
            if element == char:
                positions.append((i, j))
    return positions

def calculate_new_positions(new_positions, positions):
    if len(positions) > 1:
        for position in positions:
            for position2 in positions:
                if position != position2:
                    difference = (position2[0] - position[0], position2[1] - position[1])
                    #print('difference: ' + str(difference))
                    new_position = (position[0] - difference[0], position[1] - difference[1])
                    #print(str(new_position) + 'new_position: ')
                    new_positions.append(new_position)
                    while new_position[0] >= 0 and new_position[1] >= 0 and new_position[0] < len(list_of_lists) and new_position[1] < len(list_of_lists[0]):
                        new_position = (new_position[0] - difference[0], new_position[1] - difference[1])
                        new_positions.append(new_position)


with open('2024/08/input.txt', 'r') as file:
    lines = file.read().splitlines()

# create a two dimensinal list from input_x.txt file
list_of_lists = []
for line in lines:
    list_of_lists.append(list(line))

positions_of_chars = []
for char in string.digits + string.ascii_letters:
    if char != '.':
        positions = find_char(char, list_of_lists)
        positions_of_chars.append(positions)

new_positions = []

for char in string.digits + string.ascii_letters:
    if char != '.':
        positions = find_char(char, list_of_lists)
        calculate_new_positions(new_positions, positions)

# remove all negative positions from new_positions
new_positions = [position for position in new_positions if position[0] >= 0 and position[1] >= 0]
# remove all new_positions that are longer than len(list_of_lists) and len(list_of_lists[0])
new_positions = [position for position in new_positions if position[0] < len(list_of_lists) and position[1] < len(list_of_lists[0])]
# make new_positions unique
new_positions = list(set(new_positions))

new_output = list_of_lists.copy()

# create output.txt file with new_positions as '#'
for position in new_positions:
    if position[0] < len(new_output) and position[1] < len(new_output):
        new_output[position[0]][position[1]] = '#'

# write list_of_lists to output.txt
with open('2024/08/output.txt', 'w') as file:
    for line in new_output:
        file.write(''.join(line) + '\n')


#print(len(new_positions))
#print(new_positions)

# remove empty in positions_of_chars
positions_of_chars = [position for position in positions_of_chars if position != []]
#print(positions_of_chars)

#flatten positions_of_chars
positions_of_chars = [item for sublist in positions_of_chars for item in sublist]

all_positions = []
all_positions.extend(positions_of_chars)
all_positions.extend(new_positions)

# make all_positions unique
all_positions = list(set(all_positions))
print(len(all_positions))
