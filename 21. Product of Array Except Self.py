## Product of Array Except Self
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

nums = [1, 2, 3, 4]

print("Way-1")
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


print("Way-2")
res = [1]*len(nums)
prefix = 1

for i in range(len(nums)):
    res[i] = prefix
    prefix *= nums[i]
postfix = 1

for i in range(len(nums)-1, -1, -1):
    res[i] *= postfix
    postfix *= nums[i]
print(res)

print("Way-3")
nums = [1, 2, 3, 4]
total = 1
for ele in nums:
    total *= ele

res = []
for ele in nums:
    res.append(total//ele)
print(res)
