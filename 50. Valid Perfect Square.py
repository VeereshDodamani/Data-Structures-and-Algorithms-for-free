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
