from tqdm import tqdm

def blink(stones):
    newStones = []
    for stone in tqdm(stones, desc="Processing stones"):
        #remove trailing zeros
        stone = int(stone)
        # number of difgits
        n = len(str(stone))
        if int(stone) == 0:
            newStones.append(1)
        # if n is even
        elif n % 2 == 0:
            # take the first half of the digits
            newStones.append(str(stone)[:n//2])
            # take the second half of the digits
            newStones.append(str(stone)[n//2:])
        else:
            newStones.append(int(stone) * 2024)
    return newStones

#print(blink())

def blink_n_times(n):
    with open('2024/11/input.txt', 'r') as file:
        stones = file.read().split(' ')
    for i in tqdm(range(n)):
        stones = blink(stones)
        #print(stones)
    return stones

outcome_stones = blink_n_times(25)
#print(outcome_stones)
print(len(outcome_stones))