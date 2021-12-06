from typing import List

def bubbleSort(array :List[int]) -> List[int]:
    for outer in range(len(array) - 1):
        for inner in range(outer+1, len(array)):
            if array[outer] > array[inner]:
                array[outer], array[inner] = array[inner], array[outer]
    return array


def selectionSort(array :List[int]) -> List[int]:
    for outer in range(len(array) - 1):
        min_index = outer
        for inner in range(outer + 1, len(array)):
            if array[inner] < array[min_index]:
                min_index = inner
        array[outer], array[min_index] = array[min_index], array[outer]
    return array

def insertionSort(array :List[int]) -> List[int]:

    for index in range(1, len(array)):
        pickedValue = array[index]
        indexToCompareWith = index

        while indexToCompareWith > 0 and pickedValue < array[indexToCompareWith-1]:
            array[indexToCompareWith-1], array[indexToCompareWith] = array[indexToCompareWith], array[indexToCompareWith-1]
            indexToCompareWith -= 1
        array[indexToCompareWith] = pickedValue
    return array

def mergeSort(array :List[int]) -> List[int]:
    if len(array) == 1:
        return array

    mid = len(array) // 2
    left = array[0:mid]
    right = array[mid:]
    mergeSort(left)
    mergeSort(right)

    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i+=1
        else:
            array[k] = right[j]
            j+= 1
        k+=1

    while i < len(left):
        array[k] = left[i]
        k+=1
        i+=1

    while j < len(right):
        array[k] = right[j]
        k+=1
        j+=1
    return array

def quickSort(array: List[int]) -> List[int]:

    def partition(array: List[int], left :int, right:int) -> int:
        pivot = array[right]
        smallerSlots = left - 1
        for i in range(left, right):
            if array[i] < pivot:
                smallerSlots += 1
                array[i], array[smallerSlots] = array[smallerSlots], array[i]
        array[smallerSlots+1], array[right] = array[right], array[smallerSlots+1]

        return smallerSlots+1

    def _quickSort(array: List[int], left :int, right:int) -> List[int]:
        if len(array) < 2:
            return array
        if left < right:
            pi = partition(array, left, right)
            _quickSort(array, left, pi-1)
            return _quickSort(array, pi+1, right)
        else:
            return array

    return _quickSort(array, 0, len(array)-1)
def main():
    array = [2,1,4,3,5]

    print('Bubble Sort: {0}'.format(bubbleSort(list(array))))
    print('Selection Sort: {0}'.format(selectionSort(list(array))))
    print('Insertion Sort: {0}'.format(insertionSort(list(array))))
    print('Merge Sort: {0}'.format(mergeSort(list(array))))
    print('Quick Sort: {0}'.format(quickSort(list(array))))

if __name__ == '__main__':
    main()