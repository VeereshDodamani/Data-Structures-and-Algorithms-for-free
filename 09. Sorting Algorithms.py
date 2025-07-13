## Bubble sort
# Time: O(n^2)
# Space: O(1)

A = [-5,4,3,6,-1,-3,0,7]
print(f"Original array: {A}")

def bubble_sort(arr):
    n = len(arr)
    flag = True
    while flag:
        flag = False
        for i in range(1,n):
            if arr[i-1] > arr[i]:
                flag = True
                arr[i-1], arr[i] = arr[i], arr[i-1]

bubble_sort(A)
print(f"After bubble sort: {A}")
