    #quicksort sort only even indexes
def quicksort(Arry, start, end):
    if start >= end:
        return
    pivot = Arry[end]
    left = start
    right = end - 1
    while left <= right:
        while left <= right and Arry[left] <= pivot:
            left += 2
        while left <= right and Arry[right] >= pivot:
            right -= 2
        if left < right:
            Arry[left], Arry[right] = Arry[right], Arry[left]
    Arry[left], Arry[end] = Arry[end], Arry[left]
    quicksort(Arry, start, left - 2)
    quicksort(Arry, left + 2, end)
    return Arry

    

if __name__ == '__main__':
    arr = [11, 21, 3, 42, 15, 6, 5]
    start = 0
    end = len(arr) - 1
    print(quicksort(arr, start, end))
