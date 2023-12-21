# input = """...........
# .....###.#.
# .###.##..#.
# ..#.#...#..
# ....#.#....
# .##..S####.
# .##..#...#.
# .......##..
# .##.#.####.
# .##..##.##.
# ..........."""

with open("input.txt") as f:
    input = f.read()

steps = 64
start = 'S'

fieldAsRows = input.split("\n")
field = []
for row in fieldAsRows:
    innerArray = [*row]
    field.append(innerArray)

for x in range(steps):
    indices = []

    for index, row in enumerate(field):
        for index_2, sign in enumerate(row):
            if sign == start:
                outerindex = index
                innerindex = index_2
                indices.append([outerindex, innerindex])

    #print(indices)

    for index in indices:
        # north
        if field[index[0]-1][index[1]] == '.' or field[index[0]-1][index[1]] == x or field[index[0]-1][index[1]] == x + 1:
            field[index[0]][index[1]] = '.'
            field[index[0]-1][index[1]] = x + 1
        # east
        if field[index[0]][index[1]+1] == '.' or field[index[0]][index[1]+1] == x or field[index[0]][index[1]+1] == x + 1:
            field[index[0]][index[1]] = '.'
            field[index[0]][index[1]+1] = x + 1
        # south
        if field[index[0]+1][index[1]] == '.' or field[index[0]+1][index[1]] == x or field[index[0]+1][index[1]] == x + 1:
            field[index[0]][index[1]] = '.'
            field[index[0]+1][index[1]] = x + 1
        # west
        if field[index[0]][index[1]-1] == '.' or field[index[0]][index[1]-1] == x or field[index[0]][index[1]-1] == x + 1:
            field[index[0]][index[1]] = '.'
            field[index[0]][index[1]-1] = x + 1

    start = x + 1
    # print(x)
    # for row in field:
    #     print(row)

count = 0
for row in field:
    count += len([string for string in row if string == start]) #(string != '.' and string != '#')])
    #print(row)

print("Solution is: " + str(count))

# output= """...........
# .....###.#.
# .###.##.O#.
# .O#O#O.O#..
# O.O.#.#.O..
# .##O.O####.
# .##.O#O..#.
# .O.O.O.##..
# .##.#.####.
# .##O.##.##.
# ..........."""
#
# fieldAsRowsO = output.split("\n")
# for row in fieldAsRowsO:
#     innerArray = [*row]
#     print(innerArray)