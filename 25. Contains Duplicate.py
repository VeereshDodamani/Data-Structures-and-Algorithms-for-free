# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
# Leetcode problem: 217


print("Way-1")
nums = [1,2,3,1]
print(nums)
def duplicate(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if nums[i] == nums[j]:
                return True
    return False
            
print(duplicate(nums))
