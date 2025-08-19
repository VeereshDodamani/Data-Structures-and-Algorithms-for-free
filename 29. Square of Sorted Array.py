# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
# Leetcode problem: 977

nums = [-7,-3,2,3,11]
new = []
def sortedSquares(nums):
    for num in nums:
        new.append(num*num)
    return sorted(new)

print(sortedSquares(nums))
