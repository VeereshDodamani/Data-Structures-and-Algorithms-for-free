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


print("Way-3")
def fib2(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

n = int(input("Enter number for Fibonacci series: "))
print(f"The {n}th Fibonacci number is: {fib2(n)}")
