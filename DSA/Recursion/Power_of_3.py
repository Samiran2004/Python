def checkPowerOfThree(num):
    if num <= 0:
        return False
    if num == 1:
        return True
    if num % 3 != 0:
        return False
    return checkPowerOfThree(num//3)

num = int(input("Enter number: "))
print(f"{num} is power of three: {checkPowerOfThree(num)}")
