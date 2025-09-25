def calculateGCD(num1, num2):
    if num2 == 0:
        return num1
    return calculateGCD(num2, num1 % num2)

def calculateGCDofEvenOdd(n):
    oddSum = n * n
    evenSum = n * (n - 1)
    return calculateGCD(oddSum, evenSum)

num = int(input("Enter the number: "))
print(f"GCD of even and odd sum: {calculateGCDofEvenOdd(num)}")
