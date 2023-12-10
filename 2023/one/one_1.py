import re

a = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

# Splitting the string into lines
lines = a.strip().split('\n')

count = 0

# Printing each line
for line in lines:
	first = None
	second = None
    
	#one = line.find('one')
	one = [m.start() for m in re.finditer('one', line)]
	#two = line.find('two')
	two = [m.start() for m in re.finditer('two', line)]
	#three = line.find('three')
	three = [m.start() for m in re.finditer('three', line)]
	#four = line.find('four')
	four = [m.start() for m in re.finditer('four', line)]
	#five = line.find("five")
	five = [m.start() for m in re.finditer('five', line)]
	#six = line.find("six")
	six = [m.start() for m in re.finditer('six', line)]
	#seven = line.find("seven")
	seven = [m.start() for m in re.finditer('seven', line)]
	#eight = line.find("eight")
	eight = [m.start() for m in re.finditer('eight', line)]
	#nine = line.find("nine")
	nine = [m.start() for m in re.finditer('nine', line)]
    
	numberstr = [[1,one], [2,two], [3,three], [4,four], [5,five], [6,six], [7,seven], [8,eight], [9,nine]]
	#numberstr = [[2, two], [9, nine]]
    
#one, two, three, four, five, six, seven, eight, and nine

    
    
	#filtered_array = [arr for arr in numberstr if arr[1] != (-1)]
	filtered_array = [arr for arr in numberstr if arr[1] != []]
    
	#print(filtered_array)
	sorted_num = sorted(filtered_array, key=lambda x: x[1][0])
	sorted_back = sorted(filtered_array, key=lambda x: x[1][-1])
   	 
	for char in line:
    	if char.isdigit():
        	if (first is None):
            	if ((len(sorted_num) != 0) and (sorted_num[0][1][0] < line.find(char))):
                	first = sorted_num[0][0]
            	else:
                	first = char
        	if ((len(sorted_num) != 0) and sorted_back[-1][1][-1] > line.find(char)):
            	second = sorted_back[-1][0]
        	else:
            	second = char
           	 
	if (first is None):
    	first = sorted_num[0][0]
    	second = sorted_num[-1][0]
   	 
	#print(str(first) + str(second))
	count = count + (int(first)*10) + int(second)
    
    
print("Answer is:" + str(count))
