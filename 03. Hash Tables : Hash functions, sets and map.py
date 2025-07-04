# Hashset

s = set()
print(s)

# Add item into set: O(1)
s.add(1)
s.add(2)
s.add(3)
print(s)

# Search for item in set: O(1)
if 1 in s:
    print(True)
else:
    print(False)

# Remove ite from set: O(1)
s.remove(1)
print(s)

str1 = 'aaaaaabbbbccccccdd'
sett = set(str1) # Set Construction O(N) : N is length of string
# Will get only the unique things
print(sett)
