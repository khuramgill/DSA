def counting_sort_for_radix(input_array, exp):
    n = len(input_array)
    output = [0] * n
    count = [0] * 10  # Assuming base 10 (0 to 9 digits)

    # Count occurrences of each digit at the current place value
    for i in range(n):
        index = input_array[i] // exp
        count[index % 10] += 1

    # Modify count array to store the position of each element in the output
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = input_array[i] // exp
        output[count[index % 10] - 1] = input_array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        input_array[i] = output[i]

def radix_sort(input_array):

    max_num = max(input_array)

    # Perform counting sort for each digit place value
    exp = 1
    while max_num // exp > 0:
        counting_sort_for_radix(input_array, exp)
        exp *= 10

# Example / Test:
if __name__ == '__main__':
        
    input_array = [110, 45, 65,50, 90,602, 24, 2, 66] 
    radix_sort(input_array)
    print(input_array)
    
    
'''
Input: arr[] = [110, 45, 65,50, 90,602, 24, 2, 66]   
 
Output: [2,24,45,50,65,66,90,110,602]
 
'''
