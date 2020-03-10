'''
Harry Shepherd, 2020

Bubble Sort Algorithm
Time Complexities: Best: O(n), Average: O(n^2), Worst: O(n^2)
Space Complexity: O(1)
'''

def BubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

'''
Test
arr = [9,8,44,3,110]
print(BubbleSort(arr))
'''