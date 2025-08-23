# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.


numbers = [2,7,11,15]
target = 9

def twoSum( numbers, target):
    n = len(numbers)
    l = 0
    r = n-1

    while l<r:
        summ = numbers[l] + numbers[r]
        if summ == target:
            return [l+1, r+1]
        elif summ<target:
            l += 1
        else:
            r -= 1


print(twoSum(numbers, target))
