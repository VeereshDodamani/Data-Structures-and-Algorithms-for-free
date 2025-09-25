# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
# Leetcode problem: 83

head = [1,1,2]

print("Way-1")
print("Using loop")
unique = []
for i in head:
    if i not in unique:
        unique.append(i)

print(unique)

print("Way-2")
print("Using set")
head = set(head)
print(head)

print("Way-3")
print("Using Dict")
head = list(dict.fromkeys(head))
print(head)
