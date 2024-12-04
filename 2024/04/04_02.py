import re

with open('2024/04/input.txt', 'r') as file:
    lines = file.read().splitlines()

count = 0

#pattern:
#M.S
#.A.
#M.S

for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char == 'A':
            check = 0
            # check if there is something above, below, left and right
            # v < > <
            if len(lines) > i+1 and i-1 >= 0 and len(lines[i]) > j+1 and j-1 >= 0:
                # M.M
                # .A.
                # S.S
                if lines[i-1][j-1] == 'M' and lines[i+1][j+1] == 'S' and lines[i-1][j+1] == 'M' and lines[i+1][j-1] == 'S':
                    count += 1
                # M.S
                # .A.
                # M.S
                if lines[i-1][j-1] == 'M' and lines[i+1][j+1] == 'S' and lines[i-1][j+1] == 'S' and lines[i+1][j-1] == 'M':
                    count += 1
                # S.M
                # .A.
                # S.M
                if lines[i-1][j-1] == 'S' and lines[i+1][j+1] == 'M' and lines[i-1][j+1] == 'M' and lines[i+1][j-1] == 'S':
                    count += 1
                # S.S
                # .A.
                # M.M
                if lines[i-1][j-1] == 'S' and lines[i+1][j+1] == 'M' and lines[i-1][j+1] == 'S' and lines[i+1][j-1] == 'M':
                    count += 1




print('all counts '+str(count))
