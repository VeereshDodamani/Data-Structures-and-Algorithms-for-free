# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
# Leetcode probelm : 1004

nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2

print("Given input: ",nums)
print("Number of zeros: ",k)

def longestOne(nums,k):
    max_w = 0
    num_zeroes = 0
    n = len(nums)
    l = 0

    for r in range(n):
        if nums[r] == 0:
            num_zeroes += 1

        while num_zeroes > k:
            if nums[l] == 0:
                num_zeroes -= 1
            l += 1

        w = r-l+1
        max_w = max(max_w, w)

    return max_w


print("Max Consecutive Ones: ",longestOne(nums, k))
