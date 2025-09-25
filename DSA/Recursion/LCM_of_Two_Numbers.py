def calculateGCD(num1, num2):
    if num2 == 0:
        return num1
    return calculateGCD(num2, num1 % num2)

def calculateLCM(num1, num2):
    return num1*num2//calculateGCD(num1, num2)

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
print(f"LCM of {num1} and {num2} is: {calculateLCM(num1, num2)}")
