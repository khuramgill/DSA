import numpy as n
import time
import csv
#       Function for Adding Random integers in Array/list
def AddRandomNum(Arry,num):
    for i in range(0,num):
        rannd = n.random.randint(-100,1000)
        Arry.append(rannd)
    
#     InsertionSort Function For Sorting the Array/List
def InsertionSort(Array , strt , end):
    for i in range(strt,end):
        key = Array[i]
        j = i - 1
        while j >= 0 and key < Array[j]:
           Array[j + 1] = Array[j]
           j -= 1
        Array[j + 1] = key
        
# Merge Sort
def Merge(arr, p, q, r):
    left = arr[p:q+1]
    right = arr[q+1:r+1]

    i = j = 0
    k = p

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
      # HybridMerge Sort Fun
def HybridMergeSort(arr, start, end, n):
    if end - start <= n:
        # Use InsertionSort for small subarrays
        InsertionSort(arr, start, end)
    else:
        mid = (start + end) // 2
        HybridMergeSort(arr, start, mid, n)
        HybridMergeSort(arr, mid + 1, end, n)
        Merge(arr, start, mid, end)
        

        # Function for Save Array in File as CSV   
def SaveArryToCSV(Arry):
    with open('SortedHybridMergeSort.csv', 'w', newline='') as csvfile:
        Write = csv.writer(csvfile)
        for k in Arry:
            Write.writerow([k])
       
      
                           
  #         Main Programe     
if __name__ == '__main__':
    num = []
    k = 50
    AddRandomNum(num,500000)
    endpoint = len(num)
    start_time = time.time()
    HybridMergeSort(num,0,endpoint - 1,k)
    #   Checking Run Time
    end_time = time.time() 
    runtime = end_time - start_time 
    SaveArryToCSV(num)
    print(f"After Sorting: {num}")    
    print("Runtime of factorial at",n,"is",runtime,"seconds") 