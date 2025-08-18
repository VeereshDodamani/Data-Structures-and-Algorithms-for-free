# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# Leetcode problem: 128

print("Way-1")
nums = [0,3,7,2,5,8,4,6,0,1]
nums = sorted(nums)
print(nums)

i = nums[0]
for i in nums:
    if i+1 in nums:
        i += 1

print("Longest Consecutive Sequence:",i+1)


print("Way-2")
def longestConsecutive(nums):
    s = set(nums)
    longest = 0

    for num in nums:
        if num-1 not in s:
            next_num = num+1
            length = 1
            while next_num in s:
                length += 1
                next_num += 1
            longest = max(longest, length)
    return longest

nums = [100,4,200,1,3,2]
print(nums)
print("Longest Consecutive Sequence:",longestConsecutive(nums))
