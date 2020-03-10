'''
Harry Shepherd, 2020

Selection Sort Algorithm
Time Complexities: Best: O(n^2), Average: O(n^2), Worst: O(n^2)
Space Complexity: O(1)
'''
def SelectionSort(arr):
    for i in range(len(arr)):
        mindx = i
        for j in range(i+1, len(arr)):
            if arr[i]> arr[j]:
                mindx = j
        arr[i], arr[mindx] = arr[mindx], arr[i]
    return arr
'''
Test
arr = [9,8,44,3,110]
print(SelectionSort(arr))
'''

