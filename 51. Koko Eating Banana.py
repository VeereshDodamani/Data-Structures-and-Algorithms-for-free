# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

# Return the minimum integer k such that she can eat all the bananas within h hours.
# Leetcode probelm: 875

from math import ceil
piles = [30,11,23,4,20]
h = 5

def minEatingSpeed(piles, h):
    def k_works(k):
        hours = 0
        for p in piles:
            hours += ceil(p/k)
        return hours <= h

    l = 1
    r = max(piles)

    while l<r:
        k = (l+r) // 2
        if k_works(k):
            r = k
        else:
            l = k+1
    
    return l

print("Minimum hours required: ",minEatingSpeed(piles, h))
