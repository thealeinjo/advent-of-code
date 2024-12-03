import re

with open('2024/03/input.txt', 'r') as file:
    content = file.read()

pattern = r'mul\(\d+,\d+\)'

matches = re.findall(pattern, content)
sum = 0
for match in matches:
    match = match.split('(')[1].split(')')[0].split(',')
    multiple = int(match[0]) * int(match[1])
    #print(multiple)
    sum += multiple

print(sum)