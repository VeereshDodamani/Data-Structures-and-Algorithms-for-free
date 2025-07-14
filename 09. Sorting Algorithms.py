## Bubble sort
# Time: O(n^2)
# Space: O(1)

A = [-5,4,3,6,-1,-3,0,7]
print(f"Before bubble sort: {A}")

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
print(f"Before Insertion sort: {B}")

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

## Selection sort
# Time: O(n^2)
# Space: O(1)

C = [-6,0,2,5,-2,1,9]
print(f"Before selection sort: {C}")
def selection_sort(c_arr):
    n  = len(c_arr)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if c_arr[j]<c_arr[min_index]:
                min_index = j
        c_arr[i], c_arr[min_index] = c_arr[min_index], c_arr[i]

selection_sort(C)
print(f"After selection sort: {C}")
print("\n")

## Merge Sort
# Time: O(nlogn)
# Space: O(n)

D = [-5,9,4,-2,7,-3,1,0]
print(f"Before Merge sort{D}")
def merge_sort(d_arr):
    n = len(d_arr)
    if n == 1:
        return d_arr
    
    m = n // 2
    L = d_arr[:m]
    R = d_arr[m:]

    L = merge_sort(L)
    R = merge_sort(R)

    l, r = 0, 0
    L_len = len(L)
    R_len = len(R)

    sorted_arr = [0] * n
    i = 0

    while l < L_len and r < R_len:
        if L[l] < R[r]:
            sorted_arr[i] = L[l]
            l += 1
        else:
            sorted_arr[i] = R[r]
            r += 1
        i += 1

    while l < L_len:
        sorted_arr[i] = L[l]
        l += 1
        i += 1

    while r < R_len:
        sorted_arr[i] = R[r]
        r += 1
        i += 1

    print(f"After Merge sort{sorted_arr}")
    return sorted_arr

merge_sort(D)
print("\n")
