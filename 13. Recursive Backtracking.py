# Recirsive Backtracking

#Leetcode problem: 78
nums = [1,2,3]

n=len(nums)
res, sol = [], []

def backtrack(i):
    if i==n:
        res.append(sol[:])
        return
    
    backtrack(i+1)

    sol.append(nums[i])
    backtrack(i+1)
    sol.pop()

backtrack(0)
print(res)
