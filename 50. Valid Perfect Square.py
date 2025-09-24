# Given a positive integer num, return true if num is a perfect square or false otherwise.

# A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

# You must not use any built-in library function, such as sqrt.

def is_perfect_square(n):
    if n < 0:
        return False
    i = 0
    while i * i < n:
        i += 1
    return i * i == n

# Example usage
number = 16
if is_perfect_square(number):
    print(True)
else:
    print(False)
