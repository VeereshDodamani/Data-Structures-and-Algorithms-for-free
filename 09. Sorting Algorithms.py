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
print("\n")

## Insertion sort
# Time: O(n^2)
# Space: O(1)

B = [-8,0,3,-2,5,-5,0,7]
print(f"Original array: {A}")

def insertion_sort(b_arr):
    n = len(b_arr)
    for i in range(1,n):
        for j in range(i,0,-1):
            if b_arr[j-1] > b_arr[j]:
                b_arr[j-1], b_arr[j] = b_arr[j], b_arr[j-1]
            else:
                break
        
insertion_sort(B)
print(f"After Insertion sort: {B}")
print("\n")
