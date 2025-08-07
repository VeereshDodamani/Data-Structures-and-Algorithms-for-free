## Product of Array Except Self
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

nums = [1, 2, 3, 4]
l_mult = 1
r_mult = 1

n = len(nums)

l_arr = [0] * n
r_arr = [0] * n

for i in range(n):
    j = -i - 1
    l_arr[i] = l_mult
    r_arr[j] = r_mult
    l_mult *= nums[i]
    r_mult *= nums[j]

result = [l * r for l, r in zip(l_arr, r_arr)]
print(f"Given the array {nums}, the product of all elements except the current one is: {result}")
