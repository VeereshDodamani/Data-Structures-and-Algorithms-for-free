# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.
# Leetcode rpoblem: 383


print("Way-1")
ransomNote = "aa"
magazine = "aab"
res = []
def can(magazine,ransomNote):
    if ransomNote in magazine:
        return True
    else:
        return False

print(can(magazine,ransomNote))
