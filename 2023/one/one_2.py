# Splitting the string into lines
lines = b.strip().split('\n')

count = 0

# Printing each line
for line in lines:
    first = None
    second = None
    
    one_s = [m.start() for m in re.finditer('one', line)]
    one_i = [m.start() for m in re.finditer('1', line)]
    one = sorted(one_s + one_i, key=lambda x: x)
    two_s = [m.start() for m in re.finditer('two', line)]
    two_i = [m.start() for m in re.finditer('2', line)]
    two = sorted(two_s + two_i, key=lambda x: x)
    three_s = [m.start() for m in re.finditer('three', line)]
    three_i = [m.start() for m in re.finditer('3', line)]
    three = sorted(three_s + three_i, key=lambda x: x)
    four_s = [m.start() for m in re.finditer('four', line)]
    four_i = [m.start() for m in re.finditer('4', line)]
    four = sorted(four_s + four_i, key=lambda x: x)
    five_s = [m.start() for m in re.finditer('five', line)]
    five_i = [m.start() for m in re.finditer('5', line)]
    five = sorted(five_s + five_i, key=lambda x: x)
    six_s = [m.start() for m in re.finditer('six', line)]
    six_i = [m.start() for m in re.finditer('6', line)]
    six = sorted(six_s + six_i, key=lambda x: x)
    seven_s = [m.start() for m in re.finditer('seven', line)]
    seven_i = [m.start() for m in re.finditer('7', line)]
    seven = sorted(seven_s + seven_i, key=lambda x: x)
    eight_s = [m.start() for m in re.finditer('eight', line)]
    eight_i = [m.start() for m in re.finditer('8', line)]
    eight = sorted(eight_s + eight_i, key=lambda x: x)
    nine_s = [m.start() for m in re.finditer('nine', line)]
    nine_i = [m.start() for m in re.finditer('9', line)]
    nine = sorted(nine_s + nine_i, key=lambda x: x)
    
    numberstr = [[1,one], [2,two], [3,three], [4,four], [5,five], [6,six], [7,seven], [8,eight], [9,nine]]
    
    filtered_array = [arr for arr in numberstr if arr[1] != []]
    
    sorted_array = sorted(filtered_array, key=lambda x: x[1][0])
    sorted_back = sorted(filtered_array, key=lambda x: x[1][-1])
    
    #print(sorted_back)
    
    first = sorted_array[0][0]
    second = sorted_back[-1][0]
   	 
    #print(str(first) + str(second))
    count = count + (int(first)*10) + int(second)
    
    
print("Answer is:" + str(count))
