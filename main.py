nums = [10, 70, 30, 100, 40, 45, 90, 80, 85]
words = ["dog","at", "good", "eye", "cat", "ball", "fish"]

def bubbleSort(arr):
    for i in range(len(arr), 0, -1):
        for j in range(1, i):
            if arr[j - 1] > arr[j]:
                temp = arr[j]
                arr[j] = arr[j - 1]
                arr[j - 1] = temp
    return arr

print(bubbleSort(nums))
print(bubbleSort(words))


def selectionSort(arr):
    for i in range(0, len(arr) - 1):
        minPos = i
        for j in range(i, len(arr)):
            if arr[j] < arr[minPos]:
                minPos = i
        temp = arr[i]
        arr[i] = arr[minPos]
        arr[minPos] = temp
    return arr

print(selectionSort(nums))
print(selectionSort(words))

def insertionSort(arr):
    for i in range(1, len(arr)):
        valueToInsert = arr[i]
        insertPos = i - 1

        while i > 0 and arr[insertPos] > valueToInsert:
            temp = arr[insertPos]
            arr[insertPos] = valueToInsert
            arr[i] = temp
        
    return arr

print(insertionSort(nums))
print(insertionSort(words))