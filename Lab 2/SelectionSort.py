import numpy as n
import time
import csv
#       Function for Adding Random integers in Array/list
def AddRandomNum(Arry,num):
    for i in range(0,num):
        rannd = n.random.randint(-100,1000)
        Arry.append(rannd)


# SelectionSort Fun For Sorting the Arry/List
def SelectionSort(Arry,strt,end):
    for i in range(strt,end):
        min_idx = i
        for j in range(i+1, end):
            if Arry[min_idx] > Arry[j]:
                min_idx = j      
        Arry[i], Arry[min_idx] = Arry[min_idx], Arry[i]
        
        
  # Function for Save Array in File as CSV      
def SaveArryToCSV(Arry):
    with open('SortedInsertionSort.csv', 'w', newline='') as csvfile:
        Write = csv.writer(csvfile)
        for k in Arry:
            Write.writerow([k])
        
        
  #         Main Programe     
if __name__ == '__main__':
    num = []
    AddRandomNum(num,10000)
    endpoint = len(num)
    start_time = time.time()
    SelectionSort(num,0,len(num))
    #   Checking Run Time
    end_time = time.time()
    runtime = end_time - start_time
    # SaveArryToCSV(num)
    print(f"After Sorting: {num}")    
    print("Runtime of factorial at",n,"is",runtime,"seconds") 