def checkPowerOfTwo(num):
    # Base case...
    if num <= 0:
        return False
    if num == 1:
        return True
    if num % 2 != 0:
        return False
    return checkPowerOfTwo(num//2)

num = int(input("Enter the number: "))
print(f"{num} is power of two: {checkPowerOfTwo(num)}")
