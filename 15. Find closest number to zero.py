## Find closest number to zero
# Leetcode problem: 2239

nums = [-4,-3,9,4,8]

closest = nums[0]
for i in nums:
    if abs(i) < abs(closest):
        closest = i

if closest < 0 and abs(closest) in nums:
    print(abs(closest))
else:
    print(closest)
