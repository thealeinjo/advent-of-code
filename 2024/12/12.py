from tqdm import tqdm

with open('2024/12/input.txt', 'r') as file:
    fields = file.read().splitlines()

def are_elements_next_to_each_other(element1, element2):
    pos1 = element1[1]
    pos2 = element2[1]
    # Check if the positions are adjacent
    return (abs(pos1[0] - pos2[0]) == 1 and pos1[1] == pos2[1]) or \
        (abs(pos1[1] - pos2[1]) == 1 and pos1[0] == pos2[0])

def calculate_borders_of_an_area(elements):
    borders = []
    for element in elements:
        pos = element
        borders.append((pos[0] - 1, pos[1]))
        borders.append((pos[0] + 1, pos[1]))
        borders.append((pos[0], pos[1] - 1))
        borders.append((pos[0], pos[1] + 1))
    borders = [b for b in borders if b not in elements]
    return borders


def print_output_file(borders):
    # create a matrix from fields, but for every border in border write a 1
    # for every element in only_positions write a 2
    matrix = [[0 for i in range(len(fields[0]))] for j in range(len(fields))]
    for border in borders:
        if matrix[border[0]][border[1]] == 0:
            matrix[border[0]][border[1]] = 1
        else:
            matrix[border[0]][border[1]] = matrix[border[0]][border[1]] + 1

    # print in output file
    with open('2024/12/output.txt', 'w') as file:
        for row in matrix:
            file.write(''.join(map(str, row)) + '\n')

def check_if_around_are_same_and_add(fields, area):
    for position in area:
        # check above
        if position[0] != 0 and \
            fields[position[0]][position[1]] == fields[position[0]-1][position[1]] and \
            (position[0]-1, position[1]) not in area:
                area.append((position[0]-1, position[1]))
                check_if_around_are_same_and_add(fields, area)
        # check right
        elif len(fields[0]) - 1 > position[1] and \
            fields[position[0]][position[1]] == fields[position[0]][position[1]+1] and \
            (position[0], position[1]+1) not in area:
                area.append((position[0], position[1]+1))
                check_if_around_are_same_and_add(fields, area)
        # check down
        elif len(fields) - 1 > position[0] and \
            fields[position[0]][position[1]] == fields[position[0]+1][position[1]] and \
            (position[0]+1, position[1]) not in area:
                area.append((position[0]+1, position[1]))
                check_if_around_are_same_and_add(fields, area)
        # check left
        elif position[1] != 0 and \
            fields[position[0]][position[1]] == fields[position[0]][position[1]-1] and \
            (position[0], position[1]-1) not in area:
                area.append((position[0], position[1]-1))
                check_if_around_are_same_and_add(fields, area)
    return area




all_points = []
new_areas = []
for x in range(len(fields)):
    for y in range(len(fields[0])):
        all_points.append((x, y))

while True:
    new_area = check_if_around_are_same_and_add(fields, [(x, y)])
    if new_area not in new_areas:
        new_areas.append(new_area)
    # remove new_area from all_points
    all_points = [p for p in all_points if p not in new_area]
    print(len(all_points))
    if len(all_points) == 0:
        break
    (x, y) = all_points[0]



num_area_num_border = []
for area in new_areas:
    letter = fields[area[0][0]][area[0][1]]
    borders = calculate_borders_of_an_area(area)
    num_area_num_border.append((letter, len(area), len(borders)))
    #print(f'Area for {letter}: {len(area)}, borders: {len(borders)}, multi: {len(area) * len(borders)}')


sum = 0
for letter, num_area, num_border in num_area_num_border:
    #print(f'Letter: {letter}, Area: {num_area}, borders: {num_border}, multi: {num_area * num_border}')
    sum += num_area * num_border

print(sum)

# 1412536 too low