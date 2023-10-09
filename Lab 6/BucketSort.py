#-------------------------------------------Bucket Sort-------------------------------------------
def bucketSort(arr):
    # Create n empty buckets
    n = len(arr)
    buckets = [[] for _ in range(n)]

    for i in range(n):
        index = int(n * arr[i])
        buckets[index].append(arr[i])
        index = int(n * arr[i])
        buckets[index].append(arr[i])

    # Sort individual buckets using insertion sort
    for i in range(n):
        buckets[i] = insertionSort(buckets[i])

    # Concatenate all sorted buckets
    output = []
    for i in range(n):
        output += buckets[i]

    return output

def insertionSort(bucket):
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        while j >= 0 and bucket[j] > key:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = key
    return bucket

if __name__ == '__main__':
        
    arr = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434] 
    print(bucketSort(arr))
    
    
'''
Input: arr[]=[0.897, 0.565, 0.656,0.1234, 0.665, 0.3434]   
 
Output: [0.1234, 0.3434, 0.565,0.656, 0.665, 0.897] 
'''