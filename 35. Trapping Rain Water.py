# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
# Leetcode problem: 42


height = [0,1,0,2,1,0,1,3,2,1,2,1]

l = 0
r = 0

n = len(height)
max_l = [0] * n
max_r = [0] * n

for i in range(n):
    j = -i-1
    max_l[i] = l
    max_r[j] = r

    l = max(l, height[i])
    r = max(r, height[j])
     
summ = 0
for i in range(n):
    pot = min(max_l[i], max_r[i])
    summ += max(0, pot-height[i])

print(summ)
