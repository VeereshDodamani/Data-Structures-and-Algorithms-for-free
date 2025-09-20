# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

# Way-1
print("Way-1")
nums = [4,5,6,7,0,1,2]
target = 3
i = 0

def find(nums, target, i):
    for i in range(len(nums)):
        if nums[i] == target:
            return f'Position:{i}'
    return ("Position:-1")

print(find(nums, target, i))


# Way-2
print("Way-2")
def find2(nums, target):
    n = len(nums)
    l = 0
    r = n-1

    while l<r:
        m = (l+r) // 2
        if nums[m] > nums[r]:
            l = m+1
        else:
            r = m
    
    min_i = l

    if min_i == 0:
        l, r = 0, n-1
    elif target >= nums[0] and target <= nums[min_i-1]:
        l, r = 0, min_i - 1
    else:
        l, r = min_i, n-1

    while l<=r:
        m = (l+r) // 2

        if nums[m] == target:
            return f'Position: {m}'
        elif nums[m] < target:
            l = m+1
        else:
            r = m-1

    return ("Position:-1")

print(find2(nums, target))
