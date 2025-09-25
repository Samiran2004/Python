def findFionacciNum(n: int):
    # Base case...
    if n == 0 or n == 1:
        return n

    # Recursive case...
    return findFionacciNum(n - 1) + findFionacciNum(n - 2)

num = int(input("Enter the number: "))
print(f"The {num}th fibonacci number is: {findFionacciNum(num)}")
