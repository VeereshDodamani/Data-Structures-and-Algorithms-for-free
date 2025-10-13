# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.
# Leetcode probelm number 643
def findMaxAverage(nums, k):
    n = len(nums)
    cur_sum = 0

    for i in range(k):
        cur_sum += nums[i]

    max_avg = cur_sum / k

    for i in range(k, n):
        cur_sum += nums[i]
        cur_sum -= nums[i-k]

        avg = cur_sum / k
        max_avg = max(max_avg, avg)

    return max_avg

nums = [1,12,-5,-6,50,3]
k = 4
print("Array list: ",nums)
print("K value: ",k)

print("Maximum average subarray: ",findMaxAverage(nums,k))
