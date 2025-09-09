def binarySearch(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid, nums[mid]  
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1, None  

nums = [-1, 0, 3, 5, 9, 12]
target = 9
index, value = binarySearch(nums, target)
print("Index:", index, "Value:", value)
