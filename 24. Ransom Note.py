# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

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

print("Way-2")
ransomNote = "aab"
magazine = "baa"
def can2(ransomNote,magazine):
    counter = {}
    for c in magazine:
        if c in counter:
            counter[c] += 1
        else:
            counter[c] = 1

    for c in ransomNote:
        if c not in counter:
            return False
        elif counter[c] == 1:
            del counter[c]
        else:
            counter[c] -= 1
    return True

print(can2(ransomNote,magazine))
