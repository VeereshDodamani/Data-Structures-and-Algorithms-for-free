## Dynamic Programming

# Leetcode problem: 509
print("Way-1")
def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
        
    return fib(n-2)+fib(n-1)

n = int(input("Enter number for Fibonacci series: "))
print(f"The {n}th Fibonacci number is: {fib(n)}")


print("Way-2")
memo = {0: 0, 1: 1}

def f(x):
    if x in memo:
        return memo[x]
    memo[x] = f(x - 1) + f(x - 2)
    return memo[x]

n = int(input("Enter number for Fibonacci series: "))
print(f"The {n}th Fibonacci number is: {f(n)}")
