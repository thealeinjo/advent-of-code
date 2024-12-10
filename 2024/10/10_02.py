with open('2024/10/input.txt', 'r') as file:
    lines = file.read().splitlines()

# count all 0s and save their positions
count = 0
position_of_0 = []
for x, line in enumerate(lines):
    for y, char in enumerate(line):
        if char == '0':
            count += 1
            position_of_0.append((x, y))

def get_all_neighbors_and_its_value(x, y):
    neighbors = []
    if x - 1 >= 0:
        neighbors.append((x - 1, y, lines[x - 1][y]))
    if x + 1 < len(lines):
        neighbors.append((x + 1, y, lines[x + 1][y]))
    if y - 1 >= 0:
        neighbors.append((x, y - 1, lines[x][y - 1]))
    if y + 1 < len(lines[0]):
        neighbors.append((x, y + 1, lines[x][y + 1]))
    return neighbors


def find_paths(x, y, current_num, max_tries):
    if current_num == 9:
        all_reached_9s.append((x, y))
        return 1
    elif max_tries <= 0:
        return 0
    neighbors = get_all_neighbors_and_its_value(x, y)
    neighbors = list(filter(lambda neighbor: neighbor[2] == str(current_num + 1), neighbors))
    if len(neighbors) == 0:
        return 0
    path_count = 0
    for neighbor in neighbors:
        #print('current_position:', neighbor)
        path_count += find_paths(neighbor[0], neighbor[1], current_num + 1, max_tries - 1)
    return path_count

max_tries = 1000
sum = 0
for x, y in position_of_0:
    current_num = 0
    current_position = (x, y)
    all_reached_9s = []
    total_paths = find_paths(x, y, int(lines[x][y]), max_tries)
    #print(f"Total paths found: {total_paths}")
    # make all_reached_9s unique
    #all_reached_9s = list(set(all_reached_9s))
    #print(len(all_reached_9s))
    sum += len(all_reached_9s)

print(sum)

        