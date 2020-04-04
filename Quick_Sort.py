'''This program uses Quick Sort to sort a list and returns a list.
Quick Sort is based on the concept of Divide and Conquer and is carried
out by choosing a pivot element such that all the element in its left are smaller
than it and the ones on the right are larger.
Quick SOrt has an average time complexity of theta(nlogn) and is widely used
in the industry.
    list = QuickSort(list) is the correct syntax to call this module
'''

#BLL


def partition(arr, start, end):
    pivot = arr[start]
    low = start + 1
    high = end

    while True:
        while low <= high and arr[high] >= pivot:
            high -= 1
        while low <= high and arr[low] <= pivot:
            low += 1
        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
        else:
            break

    arr[start], arr[high] = arr[high], arr[start]
    return high


def quickSort(arr, start, end):
    if start >= end:
        return arr
    p = partition(arr, start, end)
    quickSort(arr, start, p-1)
    quickSort(arr, p+1, end)
    
    
#PL


if __name__ == "__main__":
    print("- QUICK SORT!! -".center(100, '*'))
    print("Enter an array to sort:")
    arr = list(map(int, input().split()))
    quickSort(arr, 0, len(arr)-1)
    for e in arr:
        print(e, end=' ')
