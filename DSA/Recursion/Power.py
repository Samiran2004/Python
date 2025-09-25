def calculatePower(num, power):
    if power == 0:
        return 1
    a = calculatePower(num, power//2)
    if power % 2 == 0:
        return a * a
    return a * a * num

num = int(input("Enter the number: "))
power = int(input("Enter the power value: "))
print(calculatePower(num, power))
