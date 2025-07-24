## Dynamic Programming

# Leetcode problem: 509
print("Way-1")
def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
        
    return fib(n-2)+fib(n-1)

print(fib(4))
