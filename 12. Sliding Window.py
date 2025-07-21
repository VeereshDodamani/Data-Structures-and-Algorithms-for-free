## Sliding Window
# 1. Variable length
# 2. Fixed length

# Variable length sliding window
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

print(longest)
