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

print(minEatingSpeed(piles, h))
