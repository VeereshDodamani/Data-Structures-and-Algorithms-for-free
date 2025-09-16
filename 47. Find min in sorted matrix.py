# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# You must write an algorithm that runs in O(log n) time.
# Leetcode probelm number: 153


nums = [3,4,5,1,2]

smallest = nums[0]
index = 0
for i in range(len(nums)):
    if smallest > nums[i]:
        smallest = nums[i]
        index = i

print(smallest)
print(f"Rotated {index} times")
