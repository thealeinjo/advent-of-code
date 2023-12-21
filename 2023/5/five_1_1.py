import sys
import threading
import time

# input = """
# seeds: 79 14 55 13
#
# seed-to-soil map:
# 50 98 2
# 52 50 48
#
# soil-to-fertilizer map:
# 0 15 37
# 37 52 2
# 39 0 15
#
# fertilizer-to-water map:
# 49 53 8
# 0 11 42
# 42 0 7
# 57 7 4
#
# water-to-light map:
# 88 18 7
# 18 25 70
#
# light-to-temperature map:
# 45 77 23
# 81 45 19
# 68 64 13
#
# temperature-to-humidity map:
# 0 69 1
# 1 0 69
#
# humidity-to-location map:
# 60 56 37
# 56 93 4"""

with open("input.txt") as f:
     input = f.read()

def get_second_numbers(arrays, x):
    return [sub_array[1] for sub_array in arrays if sub_array[0] == x]

def loadingbar(cycle, cycles, start_time):
    percent_complete = float(100 * (cycle / cycles))
    # Creating the bar representation
    bar = '#' * int(percent_complete) + '-' * (100 - int(percent_complete))
    elapsed_time = time.time() - start_time  # Time elapsed
    # Writing the bar to the console with the percentage
    sys.stdout.write(f"\r[{bar}] {percent_complete}% Time elapsed: {elapsed_time:.2f} seconds")
    sys.stdout.flush()

recipes = input.split('\n\n')

seeds = recipes[0].split(' ')
seeds = seeds[1:]

recipes = recipes[1:]

allAnswers = []

def calculation(seed):
    start_time = time.time()
    currentNumber = int(seed)
    for recipe in recipes:
        lines = recipe.split('\n')
        print(lines[0])
        lines = lines[1:]
        convertTable = []
        for index, line in enumerate(lines):
            destSourRang = line.split(' ')
            sourEnd = int(destSourRang[1]) + int(destSourRang[2])
            if int(destSourRang[1]) <= currentNumber <= sourEnd:
                rangeToCurrentNum = currentNumber - int(destSourRang[1])
                currentNumber = int(destSourRang[0]) + rangeToCurrentNum
                break
            #print("new convert")
            loadingbar(index, len(lines), start_time)

        #print(convertTable)
        #print(currentNumber)
        #newNumber = get_second_numbers(convertTable, currentNumber)
        #print(newNumber)
        #if newNumber != []:
        #    currentNumber = newNumber[0]
    allAnswers.append(currentNumber)


thread1 = threading.Thread(target=calculation(seeds[0]))
thread2 = threading.Thread(target=calculation(seeds[1]))
thread3 = threading.Thread(target=calculation(seeds[2]))
thread4 = threading.Thread(target=calculation(seeds[3]))
thread5 = threading.Thread(target=calculation(seeds[4]))
thread6 = threading.Thread(target=calculation(seeds[5]))
thread7 = threading.Thread(target=calculation(seeds[6]))
thread8 = threading.Thread(target=calculation(seeds[7]))

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread6.start()
thread7.start()
thread8.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()
thread5.join()
thread6.join()
thread7.join()
thread8.join()

print(allAnswers)
solution = allAnswers[0]
for answer in allAnswers:
    if solution > answer:
        solution = answer

print("Solution: " + str(solution))

