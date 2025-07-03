A = [1,2,3,4,5]
print(f"Array : {A}")

# Append
# Add element at the end
# Time Complexity : O(1)
A.append(6)
print(f"Insert element : {A}")

# Pop
# Deletes element from the end
# Time Complexity : O(1)
A.pop()
print(f"Pop element : {A}")

# Insert at particular index
# Time Complexity : O(n)
A.insert(0, 10)
print(f"Insert 10 at index 0 : {A}")

# Modify a element
# Time complexity : O(1)
A[0]=0
print(f"Modified array : {A}")

# Accessing a element given a index
# Time complexity : O(1)
print(f"Accessing element of index 2 : {A[2]}")

# Check of the array has that element
if 10 in A:
    print(f"Yes")
else:
    print("Element not present in array")
