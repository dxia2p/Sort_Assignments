nums = [10, 70, 30, 100, 40, 45, 90, 80, 85]
words = ["dog","at", "good", "eye", "cat", "ball", "fish"]

def bubbleSort(arr):
    for i in range(len(arr), 1, -1):
        for j in range(1, i):
            if arr[j - 1] > arr[j]:
                temp = arr[j]
                arr[j] = arr[j - 1]
                arr[j - 1] = temp

bubbleSort(nums)
print(nums)
bubbleSort(words)
print(words)

nums = [10, 70, 30, 100, 40, 45, 90, 80, 85]
words = ["dog","at", "good", "eye", "cat", "ball", "fish"]

def selectionSort(arr):
    for i in range(0, len(arr) - 1):
        minPos = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minPos]:
                minPos = j
        temp = arr[i]
        arr[i] = arr[minPos]
        arr[minPos] = temp
    
selectionSort(nums)
print(nums)
selectionSort(words)
print(words)

nums = [10, 70, 30, 100, 40, 45, 90, 80, 85]
words = ["dog","at", "good", "eye", "cat", "ball", "fish"]

def insertionSort(arr):
    for i in range(1, len(arr)):
        valueToInsert = arr[i]
        insertPos = i

        while insertPos > 0 and arr[insertPos - 1] > valueToInsert:
            arr[insertPos] = arr[insertPos - 1]
            insertPos -= 1
        arr[insertPos] = valueToInsert
    return arr
insertionSort(nums)
print(nums)
insertionSort(words)
print(words)