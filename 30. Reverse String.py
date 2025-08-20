# Write a function that reverses a string. The input string is given as an array of characters s.
# Leetcode problem: 344

print("Way-1")
s = ["H","a","n","n","a","h"]
print("Given string: ",s)
i = len(s)-1
a = []

while i>=0:
    a.append(s[i])
    i -= 1
print("Reversed string",a)


print("Way-2")
def reverseString(s):
    left, right = 0, len(s)-1
    while left<right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return(s)
print(reverseString(s))
