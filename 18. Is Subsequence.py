## Is Subsequence
# Leetcode problem: 3

s = "abc"
t = "ahbgdc"

S = len(s)
T = len(t)

if s == '':
    print(True)
    exit()

if S > T:
    print(False)
    exit()

j = 0
for i in range(T):
    if t[i] == s[j]:
        j += 1
        if j == S:
            print(True)
            break
else:
    print(False)
