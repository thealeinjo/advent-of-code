# Splitting the string into lines
lines = real_in.strip().split('\n')

impossible_count = 0
game_count = 0
power = 0

for line in lines:
	#print(line)
	#split game:
	split_lines = line.strip().split(': ')
	#print(split_lines)
	game_number = int(split_lines[0][5:])
	game_count += game_number
	#print(game_number)
	line_short = split_lines[1]
	sets = line_short.strip().split('; ')
	#print(sets)
    
	impossible = 0
	highest_blue = 0
	highest_red = 0
	highest_green = 0

	for set in sets:
    	colors = set.strip().split(", ")
    	#print('colors: ' + str(colors))
   	 
    	for color in colors:
        	if color.find('blue') != (-1):
            	if int(color.strip().split(' ')[0]) > highest_blue:
                	#impossible = game_number
                	highest_blue = int(color.strip().split(' ')[0])
        	if color.find('red') != (-1):
            	if int(color.strip().split(' ')[0]) > highest_red:
                	highest_red = int(color.strip().split(' ')[0])
        	if color.find('green') != (-1):
            	if int(color.strip().split(' ')[0]) > highest_green:
                	highest_green = int(color.strip().split(' ')[0])
	power += (highest_blue*highest_red*highest_green)
	#impossible_count += impossible
	#print(impossible_count)
#possible = game_count - impossible_count
print("Answer is: " + str(power))
