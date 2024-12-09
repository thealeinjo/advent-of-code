with open('2024/09/input.txt', 'r') as file:
    lines = file.read()

conv_list = []
file_id = 0

for place, char in enumerate(lines):
    # if char is devided by 2, then print it
    if int(place) % 2 == 0:
        for i in range(int(char)):
            conv_list.append(file_id)
        file_id += 1
    else:
        for i in range(int(char)):
            conv_list.append('.')

#print(conv_list)
# go through files backwards
for i in range(len(conv_list)-1, -1, -1):
    if conv_list[i] != '.':
        for j, char in enumerate(conv_list):
            if char == '.':
                conv_list[j] = conv_list[i]
                conv_list[i] = '.'
                break

#print(conv_list)

# remove first element of conv_list
conv_list.pop(0)

sum = 0

for i, char in enumerate(conv_list):
    if char != '.':
        sum += i * int(char)
    else:
        break

print(sum)