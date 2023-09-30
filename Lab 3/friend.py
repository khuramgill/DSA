def check_similarity(list1,list2):
    for i in list1:
        for j in list2:
            if i == j:
                # print(i,j)
                return True
    return False

    
def friendSlower(Input):
    temp_tuples = []
    
    for i in Input:
        ranges = list(range(i[0],i[1] + 1))
        # print(ranges)
        for j in Input:
            if i == j:
                continue
            else:
                rangee = list(range(j[0],j[1] + 1)) 
                # print(rangee)
                if check_similarity(ranges, rangee) :
                    # print(str(Input.index(i)) + "," + str(Input.index(j)))
                    temp_tuples.append((Input.index(i) + 1 ,Input.index(j) + 1))
                    # print(temp_tuples)
         
    #print(0,1) == (1,0)
    return_tuple_list = []
    for i in temp_tuples:
        x1,y1 = i[0],i[1]
        # print(x1,y1)
        for j in temp_tuples:
            x2,y2  = j[0],j[1]
            
            if x1 == y2 and y1 == x2:
                # print(i)
                # print(j)
                return_tuple_list.append((x1,y1))
                
                temp_tuples.remove(i)
                temp_tuples.remove(j)
                # print(temp_tuples)
    # print(temp_tuples)
    return_tuple_list.append(temp_tuples[0])
    # print(return_tuple_list)
    return return_tuple_list   
        
 
       
def friendsFaster(Input):
    #2D = np.array(Input)
    #print(Input[list(np.argsort(Input,0,'mergesort'))])
    #ind = np.argsort(Input,0,'mergesort')
    Input = sorted(Input,key = lambda x:x[0])
    # print(Input)
    tuples = []
    
    for i in range (0, len(Input) + 1 , 2):
        if i < len(Input) - 1:
            loop_var = Input[i]
            next_var = Input[i + 1]
            
            ranges  = list(range(loop_var[0], loop_var[1] + 1))
            if next_var[0] in ranges:
                tuples.append((Input.index(loop_var) +1 , Input.index(next_var) + 1))
                # print(tuples)
        
        elif i == len(Input) - 1: # check last element by 2 counter increment
            loop_var = Input[i - 1] # check immediate precedding
            next_var = Input[i]
            
            ranges  = list(range(loop_var[0], loop_var[1] + 1))
            if next_var[0] in ranges:
                tuples.append((Input.index(loop_var) +1 , Input.index(next_var) + 1))
            
            
            loop_var = Input[i - 2] # check one step backwards
            next_var = Input[i]
            
            ranges  = list(range(loop_var[0], loop_var[1] + 1))
            if next_var[0] in ranges:
                tuples.append((Input.index(loop_var) +1 , Input.index(next_var) + 1))      
                
    return tuples
            
               


if __name__ == '__main__':
    test = [[1,4],[2,5],[7,9],[9,10],[6,10]]
    print(friendsFaster(test))
    print(test)