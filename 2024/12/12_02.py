import time

# Record the start time
start_time = time.time()

with open('2024/12/input.txt', 'r') as file:
    fields = file.read().splitlines()

def are_elements_next_to_each_other(element1, element2):
    pos1 = element1
    pos2 = element2
    # Check if the positions are adjacent
    return (abs(pos1[0] - pos2[0]) == 1 and pos1[1] == pos2[1]) or \
        (abs(pos1[1] - pos2[1]) == 1 and pos1[0] == pos2[0])

def calculate_borders_of_an_area(elements):
    borders = []
    for element in elements:
        pos = element
        borders.append(((pos[0] - 1, pos[1]), 'up'))
        borders.append(((pos[0] + 1, pos[1]), 'down'))
        borders.append(((pos[0], pos[1] - 1), 'left'))
        borders.append(((pos[0], pos[1] + 1), 'right'))
    borders = [b for b in borders if b[0] not in elements]
    return borders

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
    #print(len(all_points))
    if len(all_points) == 0:
        break
    (x, y) = all_points[0]



num_area_num_border = []
for area in new_areas:
    letter = fields[area[0][0]][area[0][1]]
    borders = calculate_borders_of_an_area(area)

    # group borders by are_elements_next_to_each_other
    borders_grouped = []
    for border in borders:
        found = False
        for group in borders_grouped:
            for element in group:
                #print(border)
                if are_elements_next_to_each_other(element[0], border[0]):
                    if len(group) > 1:
                        # check line
                        if group[0][0][0] == group[1][0][0] and group[0][0][0] == border[0][0] \
                            and group[0][1] == border[1] and border not in group:
                            #horizontal
                            group.append(border)
                            found = True
                            break
                        elif group[0][0][1] == group[1][0][1] and group[0][0][1] == border[0][1] \
                            and group[0][1] == border[1] and border not in group:
                            #vertical
                            group.append(border)
                            found = True
                            break
                    else:
                        if group[0][1] == border[1]:
                            group.append(border)
                            found = True
                            break
        if not found:
            borders_grouped.append([border])
    
    #print(f'Bordersgrouped for {letter}, len(borders_grouped): {len(borders_grouped)}, borders: {borders_grouped}')

    num_area_num_border.append((letter, len(area), len(borders_grouped)))


sum = 0
for letter, num_area, num_border in num_area_num_border:
    #print(f'Letter: {letter}, Area: {num_area}, borders: {num_border}, multi: {num_area * num_border}')
    sum += num_area * num_border

print(sum)

# Record the end time
end_time = time.time()

# Calculate and print the elapsed time
elapsed_time = end_time - start_time
print(f"Overall execution time: {elapsed_time:.2f} seconds")

# 882843 too high
# 870311 too high
# 870310 too high


# borders: [[(6, 0)], [(7, -1), (8, -1), (9, -1)], [(7, 1), (8, 1), (8, 1), (8, 2)], [(10, 0), (10, 1), (10, 2)], [(9, 3)]]

# R, len(borders_grouped): 9, borders: [[(-1, 0), (-1, 1), (-1, 2), (-1, 3)], [(0, -1), (1, -1)], [(2, 0), (2, 1), !(2, 1)],
# [(0, 4), (1, 4), !(1, 4)], [(3, 3), (3, 4)], [(4, 2)], [(3, 1)], [(3, 3), (3, 4)], [(2, 5)]]
#[[(2, 4), (1, 4)] (A >), [(2, 4), (1, 4)] (A >), [(4, 2), (3, 2)] (B <), [(4, 2), (3, 2)] (B <), 
# [(2, 3), (1, 3)] (A <), [(4, 1), (3, 1)] (B <),
# [(1, 4), (1, 3)] (A ^), [(4, 1), (3, 1)] (B <), [(1, 3), (2, 3)] (A <), [(3, 1), (3, 2)] (B ^),]
