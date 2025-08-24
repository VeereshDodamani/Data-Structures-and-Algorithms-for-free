# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

nums = [-1,0,1,2,-1,-4]
n=len(nums)
i=0
target=0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if nums[i]+nums[j]+nums[k] == target:
                triplet = print(nums[i],nums[j],nums[k])
