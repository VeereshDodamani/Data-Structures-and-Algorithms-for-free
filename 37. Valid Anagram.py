# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

def is_anagram(s, t):
    return sorted(s) == sorted(t)

print(is_anagram("act", "cat"))
