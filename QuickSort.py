"""
# Quick sort algorithm
#The best-case complexity of the quick sort algorithm is O(n logn)
Step 1 − Make any element as pivot
Step 2 − Partition the array on the basis of pivot
Step 3 − Apply quick sort on left partition recursively
Step 4 − Apply quick sort on right partition recursively
#We take pivot(first/last/random/median) and arrange them. Small values than pivot moves to left side
# greater values move to right side of pivot
"""


def pivotPosition(arr, first, last):
    pivot = arr[first]  # taking pivot as a first element
    left = first + 1
    right = last

    while True:
        while left <= right and arr[left] <= pivot:
            left += 1
        while left <= right and arr[right] >= pivot:
            right -= 1
        if left > right:
            break
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[first], arr[right] = arr[right], arr[first]
    return right


def quickSort(arr, first, last):
    if first < last:
        pValue = pivotPosition(arr, first, last)
        quickSort(arr, first, pValue - 1)
        quickSort(arr, pValue + 1, last)


# Drive code

arr = [2, 66, 4, 88, 132, 1, 9, 55, 11, 321]
n = len(arr)
quickSort(arr, 0, n - 1)
print(arr)
