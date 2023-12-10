input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

# Splitting the string into lines
lines = input.strip().split('\n')

impossible_count = 0
game_count = 0

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
	print(sets)
    
	impossible = 0

	for set in sets:
    	colors = set.strip().split(", ")
    	#print('colors: ' + str(colors))
    	for color in colors:
        	if color.find('blue') != (-1):
            	if int(color.strip().split(' ')[0]) > 14:
                	impossible = game_number
        	if color.find('red') != (-1):
            	if int(color.strip().split(' ')[0]) > 12:
                	impossible = game_number
        	if color.find('green') != (-1):
            	if int(color.strip().split(' ')[0]) > 13:
                	impossible = game_number
    
	impossible_count += impossible
	#print(impossible_count)
possible = game_count - impossible_count
print("Answer is: " + str(possible))
