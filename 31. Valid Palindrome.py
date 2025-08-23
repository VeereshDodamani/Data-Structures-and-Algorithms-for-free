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
