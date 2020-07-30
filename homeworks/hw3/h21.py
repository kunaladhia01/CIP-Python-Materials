def recursive_function(n):
    if n == 1 or n == 2:
        return 1
    return recursive_function(n-2) ** 2 + recursive_function(n-1)**2
print(recursive_function(10))
