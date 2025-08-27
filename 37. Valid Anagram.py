# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

from collections import Counter
print("Way-1")
s = "act"
t = "cat"
def is_anagram(s, t):
    return sorted(s) == sorted(t)

print(is_anagram(s, t))


print("Way-2")
def is_anagram1(s, t):
    if len(s) != len(t):
        return False
    
    s_dict = Counter(s)
    t_dict = Counter(t)

    return s_dict == t_dict

print(is_anagram1(s, t))
