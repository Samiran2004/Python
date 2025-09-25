def calculateGCD(n1, n2):
    if n2 == 0:
        return n1
    return calculateGCD(n2, n1%n2)

num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))
print(f"GCD of {num1} and {num2} is: {calculateGCD(num1, num1)}")
