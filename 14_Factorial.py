def factorial(n):
    if n < 0:
        return None 
    elif n <= 1:
        return 1
    else: 
        return n * factorial(n - 1)

a = factorial(3)
print(a)