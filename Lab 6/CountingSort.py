def CountSort(input_array):

    min_val, max_val = min(input_array), max(input_array)
    k = max_val - min_val + 1

    count = [0] * k

    for i in input_array:
        count[i - min_val] += 1
    for i in range(1, k):
        count[i] += count[i - 1]


    output = [0] * len(input_array)

    for i in reversed(input_array):
        output[count[i - min_val] - 1] = i
        count[i - min_val] -= 1

    return output

# Example/Testing:
if __name__ == '__main__':
        
    Arry = [-5, -10, 0, -3, 8, 5, -1, 10]
    Arry = CountSort(Arry)
    print(Arry)




'''
arr[] = [-5, -10, 0, -3, 8, 5,  -1, 10]             
Output:[-10, -5, -3, -1, 0, 5, 8, 10]
'''
