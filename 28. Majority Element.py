# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
# Leetcode problem: 169

print("Way-1")
def majorityElement(nums):
    count = 0
    candidate = None
    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif candidate == num:
            count += 1
        else:
            count -= 1
    return candidate

nums = [3,1,2,1,2,2,1,2,2,2,1]
print(nums)
print("Majority element from given nums: ",majorityElement(nums))
print("\n")

print("Way-2")
mydict = {}
def majorityElement2(nums):
    for num in nums:
        if num not in mydict:
            mydict[num] = 1
        else:
            mydict[num] += 1
    return max(mydict)
nums = [3,2,3]
print(nums)
print("Majority element from given nums: ",majorityElement2(nums))
