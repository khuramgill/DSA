import numpy as n
import time
import csv
#       Function for Adding Random integers in Array/list
def AddRandomNum(Arry,num):
    for i in range(0,num):
        rannd = n.random.randint(-100,1000)
        Arry.append(rannd)
        
 # Merge Fun For Merging Two Arrys       
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
        
        
# MergeSort Fun For Sorting Arry
def MergeSort(arr, start, end):
    if start < end:
        mid = (start + end) // 2
        MergeSort(arr, start, mid)
        MergeSort(arr, mid + 1, end)
        Merge(arr, start, mid, end)


        
        
  # Function for Save Array in File as CSV          
def SaveArryToCSV(Arry):
    with open('SortedMergeSort.csv', 'w', newline='') as csvfile:
        Write = csv.writer(csvfile)
        for k in Arry:
            Write.writerow([k])
        
        
  #         Main Programe     
if __name__ == '__main__':
    num = []
    AddRandomNum(num,500000)
    endpoint = len(num)
    start_time = time.time()
    MergeSort(num, 0, endpoint - 1)
    #   Checking Run Time
    end_time = time.time() 
    runtime = end_time - start_time 
    # SaveArryToCSV(num)
    print(f"After Sorting: {num}")    
    print("Runtime of factorial at",n,"is",runtime,"seconds") 