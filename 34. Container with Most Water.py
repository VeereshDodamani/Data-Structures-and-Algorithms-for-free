# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.

# Leetcode problem: 11


def maxArea(height):
    n = len(height)
    l = 0
    r = n-1
    max_area = 0

    while l<r:
        width = r-l
        curr_height = min(height[l], height[r])
        area = width * curr_height
        max_area = max(max_area, area)

        if height[l]<height[r]:
            l += 1
        else:
            r -= 1

    return max_area


height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))
