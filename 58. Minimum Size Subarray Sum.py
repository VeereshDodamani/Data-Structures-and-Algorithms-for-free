# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
# Leetcode problem: 209

def minSubArrayLen(target, nums):
    min_length = float('inf')
    summ = 0
    l = 0

    for r in range(len(nums)):
        summ += nums[r]

        while summ >= target:
            min_length = min(min_length, r-l+1)
            summ -= nums[l]
            l += 1

    return min_length if min_length < float('inf') else 0


target = 7
print("Target given: ", target)
nums = [2,3,1,2,4,3]
print("Array given: ", nums)

print("Minimum size sub array is: ",minSubArrayLen(target, nums))
