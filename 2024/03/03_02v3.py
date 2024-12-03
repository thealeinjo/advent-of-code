import re

with open('2024/03/input.txt', 'r') as file:
    content = file.read()#.splitlines()

# Pattern to match "don't(.*?)do"
notpattern = r"don't(.*?)do\("

sum = 0
#for content in lines:
# Remove everything that matches the pattern
newcontent = re.sub(notpattern, '', content)

pattern = r'mul\(\d+,\d+\)'

matches = re.findall(pattern, newcontent)

for match in matches:
    match = match.split('(')[1].split(')')[0].split(',')
    multiple = int(match[0]) * int(match[1])
    #print(multiple)
    sum += multiple

print(sum)

#122730190

#109663031