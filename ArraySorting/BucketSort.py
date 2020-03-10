'''
Harry Shepherd, 2020

Bucket Sort Algorithm
Time Complexities: Best: O(n^2), Average: O(n^2), Worst: O(n^2)
Space Complexity: O(1)
'''
def BucketSort(arr):
    bucket = []
    slots = 10

    for i in range(slots):
        bucket.append([])

    for j in arr:
        indB = int(slots * j)
        bucket[indB].append(j)

    for k in range(slots):
        bucket[i] = sorted(bucket[i])

    k = 0
    for i in range(slots):
        for j in range(len(bucket[i])):
            arr[k] = bucket[i][j]
            k+=1
    return arr
'''
Test
arr = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
print(BucketSort(arr))
'''