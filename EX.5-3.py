def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage
number = int(input("Enter an integer: "))
result = factorial(number)
print(f"{number}! =", result)
