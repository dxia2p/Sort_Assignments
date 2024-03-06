# SORT ANALYZER STARTER CODE

import time
from sort_functions import bubbleSort, insertionSort, selectionSort

# RETURN DATA FROM FILE AS AN ARRAY OF INTERGERS
def loadDataArray(fileName):
    temp = []

    # Read file line by line
    fileref = open(fileName, "r")
    for line in fileref:
        line = line.strip()  # Clean up line
        temp.append(int(line))  # Add integer to temp list

    fileref.close()

    return temp


# LOAD DATA FILE INTO GLOBAL VARIABLES
randomData = loadDataArray("data-files/random-values.txt")
reversedData = loadDataArray("data-files/reversed-values.txt")
nearlySortedData = loadDataArray("data-files/nearly-sorted-values.txt")
fewUniqueData = loadDataArray("data-files/few-unique-values.txt")

# VERIFY LOADED DATA BY PRINTING FIRST 50 ELEMENTS
print(randomData[0:50])
print(reversedData[0:50])
print(nearlySortedData[0:50])
print(fewUniqueData[0:50])


# EXAMPLE OF HOW TO TIME DURATION OF A SORT ALGORITHM
# startTime = time.time()
# bubbleSort(randomData)
# endTime = time.time()
# print(f"Bubble Sort Random Data: {endTime - startTime} seconds")

def getTimeToSort(sortFunc, data):
    total = 0
    for i in range(0, 10):
        startTime = time.time()
        sortFunc(list(data))
        endTime = time.time()
        print(f"Sort Data: {endTime - startTime} seconds")
        total += endTime - startTime
    print(f"Average: {total / 10}")

#getTimeToSort(bubbleSort, randomData)
#getTimeToSort(bubbleSort, reversedData)
getTimeToSort(insertionSort, fewUniqueData)

