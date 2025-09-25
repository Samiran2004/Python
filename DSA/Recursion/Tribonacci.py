def tribonacciNumber(n: int) -> int:
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return tribonacciNumber(n - 1) + tribonacciNumber(n - 2) + tribonacciNumber(n - 3)

num = int(input("Enter the nth number: "))

print(f"The {num}th tribonacci number is: {tribonacciNumber(num)}")
