# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.


print("Way-1")
s = "A man, a plan, a canal: Panama"
s = s.lower()
print(s)

def pal(s):
    c = []
    for char in s:
        if char.isalpha():
            c.append(char)

    print(c)

    i=0
    n=0
    for char in c:
        while n != len(s)/2:
            if c[i] == c[-(i+1)]:
                print("yes")
            else:
                print("no")
            n += 1
        break
    if n == len(s)/2:
        return ("Valid Palindrome: True")
    else:
        return ("Valid Palindrome: False")

print(pal(s))
print("\n")

print("Way-2")
s = "race a car"
def isPalindrome(s):
    print(s)
    n = len(s)
    L = 0
    R = n-1

    while L<R:
        if not s[L].isalnum():
            L += 1
            continue
        if not s[R].isalnum():
            R -= 1
            continue
        
        if s[L].lower() != s[R].lower():
            return ("Valid Palindrome: False")
        
        L += 1
        R -= 1
    return ("Valid Palindrome: True")

print(isPalindrome(s))
