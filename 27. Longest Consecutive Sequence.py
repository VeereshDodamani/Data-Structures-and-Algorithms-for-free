# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# Leetcode problem: 128
nums = [0,3,7,2,5,8,4,6,0,1]
nums = sorted(nums)
print(nums)

i = nums[0]
for i in nums:
    if i+1 in nums:
        i += 1

print("Longest Consecutive Sequence:",i+1)
