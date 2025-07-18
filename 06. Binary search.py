# Binary search: Traditional search, Over-under technique

arr = [-3, -1, 0, 1, 4]
target = -9
# Naive search
# if 0 in arr:
#     print(True)

# Traditional Binary Search
# Time: O(log(N))
# Space: O(1)
def binary_search(arr, target):
    n = len(arr)
    l = 0
    r = n-1

    while l<=r:
        m = (l+r)//2
        # m = l + (r-l)//2
        # Used when there are lot's of elements

        if arr[m] == target:
            return(f"Target {target} is present")
        elif target < arr[m]:
            r = m-1
        else:
            l = m+1
    return(f"Tagret {target} is not there in array")

print(binary_search(arr,target))


# Over-under technique
# Based on condition: All the similar elements are going to be in one side
# example = [F,F,F,T,T,T]

b = [False,False,False,False,True,True,True]
def binary_search_condition(arr):
    n = len(arr)
    l = 0
    r = n-1

    while l<r:
        m = (l+r)//2

        if b[m]:
            r = m
        else:
            l = m+1
    return l

print(binary_search_condition(b))
