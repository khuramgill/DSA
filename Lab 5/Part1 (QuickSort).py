def Partition(Arry,p,r):
    x = Arry[r]
    i = p - 1   
    for j in range(p,r):
        if Arry[j] <= x :
            i = i+1
            Arry[i] , Arry[j] = Arry[j] , Arry[i]
            
    Arry[i + 1] , Arry[r] = Arry[r] , Arry[i + 1]
    return i+1

def QuickSort(Arry,p,r):
    if p < r:
        q = Partition(Arry, p, r)
        QuickSort(Arry, p, q -1)
        QuickSort(Arry, p + 1, r)


if __name__ == '__main__':
    
    my_list = [3, 6, 8, 10, 1, 2, 1]
    
    QuickSort(my_list,0,len(my_list) - 1)
    print(my_list)
        
            
            
    