import numpy as n
import csv

#       Function for Adding Random integers in Array/list
def AddRandomNum(Arry,num):
    for i in range(0,num):
        rannd = n.random.randint(-100,1000)
        Arry.append(rannd)
        
        
   # Function for Save Array in File as CSV         
def SaveArryToCSV(Arry):
    with open('SortedInsertionSort.csv', 'w', newline='') as csvfile:
        Write = csv.writer(csvfile)
        for k in Arry:
            Write.writerow([k])
        
        
        # Main Program
if __name__ == '__main__':
    num = []
    AddRandomNum(num,30000)
    SaveArryToCSV(num)
    print(num)
    