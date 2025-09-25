def factorial(n):
    if n == 0:
        return 1
    return n*factorial(n - 1)

num = int(input("Enter the value: "))
print(f"Factorial of {num} is {factorial(num)}")

