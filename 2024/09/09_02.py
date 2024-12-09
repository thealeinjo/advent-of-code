with open('2024/09/input.txt', 'r') as file:
    lines = file.read()

file_id = 0
whole_list = []

for place, char in enumerate(lines):
    # if char is devided by 2, then print it
    if int(place) % 2 == 0:
        #file_list.append((int(char), file_id))
        whole_list.append((int(char), file_id))
        file_id += 1
    else:
        whole_list.append((int(char), '.'))

#print(whole_list)

# (amount, file_id / '.')
# go through files backwards
for counter_back in range(len(whole_list)-1, -1, -1):
    current_file = whole_list[counter_back]
    if current_file[1] != '.':
        #print('current_file: ' + str(current_file))
        for counter_forward, current_place in enumerate(whole_list):
            if current_place[1] == '.' and counter_forward < counter_back:
                #print('current_place: ' + str(current_place))
                # current place is space
                if current_place[0] == current_file[0]:
                    # space is same size as file
                    whole_list[counter_forward] = current_file # replace space with file
                    whole_list[counter_back] = (current_place[0], '.') # replace old place with space
                    #print(whole_list)
                    break
                elif current_place[0] >= current_file[0]:
                    # space is bigger than file
                    whole_list[counter_forward] = current_file # replace space with file
                    rest = current_place[0] - current_file[0]
                    whole_list.insert(counter_forward+1, (rest, '.'))
                    whole_list[counter_back+1] = (current_file[0], '.')
                    #print(whole_list)
                    break

#print(whole_list)

sum = 0

counter = 0

for i, twin in enumerate(whole_list):
        for j in range(twin[0]):
            if twin[1] != '.':
                sum += counter * int(twin[1])
                #print('sum' + str(sum) + ' =counter' + str(counter) + '*twin[1]' + str(twin[1]))
            counter += 1
        

print(sum)