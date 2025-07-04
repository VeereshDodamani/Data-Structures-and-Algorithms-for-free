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


print("\n")
# Hashmap : Dictionaries
print("HASHMAP's")
d = {'code':1, 'scooby':2, 'harry':3}
print(d)

# Add key:value pair in d: O(1)
d['arsh'] = 4
print(d)

# Check for presence of key in dict
if 'harry' in d:
    print(True)
else:
    print(False)

# Check for value corrosponding to the key: O(1)
print(d['scooby'])

# traverse the hashmap
for key,val in d.items():
    print(f"{key}->{val}")

# default dict
from collections import defaultdict
default = defaultdict(int)
print(f"Default value 0 for all index: {default[2]}")

# Counter
from collections import Counter
print(str1)
count = Counter(str1)
print(count)
