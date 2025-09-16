# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.


def searchMatrix(matrix, target):
    m = len(matrix)
    n = len(matrix[0])
    t = m*n
    l = 0
    r = t - 1

    while l<=r:
        m = (l+r) // 2
        i = m // n
        j = m % n 

        mid_num = matrix[i][j]

        if target == mid_num:
            return True
        elif target < mid_num:
            r = m - 1
        else:
            l = m + 1
    
    return False


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3

print(searchMatrix(matrix, target))
