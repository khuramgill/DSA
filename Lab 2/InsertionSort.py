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
        

        # Function for Save Array in File as CSV   
def SaveArryToCSV(Arry):
    with open('SortedInsertionSort.csv', 'w', newline='') as csvfile:
        Write = csv.writer(csvfile)
        for k in Arry:
            Write.writerow([k])
       
      
                           
  #         Main Programe     
if __name__ == '__main__':
    num = []
    AddRandomNum(num,30000)
    endpoint = len(num)
    start_time = time.time()
    InsertionSort(num,0,len(num))
    #   Checking Run Time
    end_time = time.time() 
    runtime = end_time - start_time 
    # SaveArryToCSV(num)
    print(f"After Sorting: {num}")    
    print("Runtime of factorial at",n,"is",runtime,"seconds") 