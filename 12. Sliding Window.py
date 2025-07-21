## Sliding Window
# 1. Variable length
# 2. Fixed length

# Variable length sliding window
# Leetcode question: 3 
s = "abcabcbb"
l = 0
longest = 0
sett = set()
n = len(s)

for r in range(n):
    while s[r] in sett:
        sett.remove(s[l])
        l += 1

    w = (r-l)+1
    longest = max(longest, w)
    sett.add(s[r])

print(f"Longest: {longest}")

# Fixed length sliding window
# Leetcode question: 643
nums = [1,12,-5,-6,50,3]
k = 4

n = len(nums)
cur_sum = 0

for i in range(k):
    cur_sum += nums[i]

max_avg = cur_sum / k

for i in range(k,n):
    cur_sum += nums[i]
    cur_sum -= nums[i-k]

    avg = cur_sum / k
    max_avg = max(max_avg, avg)

print(f"Max-avg: {max_avg}")
