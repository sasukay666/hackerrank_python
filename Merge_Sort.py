'''This program uses Merge Sort to sort a list and returns a list.
Merge Sort is based on the concept of Divide and Conquer and is carried
out by dividing the input into smaller parts until a single unit is left.
Then these small units are merged together to form a sorted array in step
by step manner.
Merge Sort has an average time complexity of theta(nlogn) and is widely used
in the industry.
    list = mergeSort(list) is the correct syntax to call this module
'''
#BLL


def merge(arr1, arr2):
    '''merge function takes two lists as input and
    merges them by 2-way merging and returns a single list'''
    i, j = 0, 0
    arr3 = []
    while i < len(arr1) and j < len(arr2):  #while there are elements left in both arrays
        if arr1[i] < arr2[j]:
            arr3.append(arr1[i])
            i += 1
        else:
            arr3.append(arr2[j])
            j += 1
    while i < len(arr1):    #while there are elements in first array
        arr3.append(arr1[i])
        i += 1
    while j < len(arr2):    #while there are elements in second array
        arr3.append(arr2[j])
        j += 1
    return arr3


def mergeSort(arr):
    if len(arr) == 1:   #if length of input is 1, no need to perform any further partitions
        return arr
    arr1 = arr[:int(len(arr)/2)]
    arr2 = arr[int(len(arr)/2):]
    arr1 = mergeSort(arr1)
    arr2 = mergeSort(arr2)
    return merge(arr1, arr2)

#PL


if __name__ == "__main__":
    print("- MERGE SORT!! -".center(100, '*'))
    print("Enter an array to sort:")
    arr = list(map(int, input().split()))
    arr = mergeSort(arr)
    print("Sorted array:")
    for e in arr:
        print(e, end=' ')
