def subtractProductAndSum(n: int)-> int:
    productOfDigits = calculateProductOfDigits(n=n)
    sumOfDigits = calculateSumOfDigits(n=n)
    return productOfDigits - sumOfDigits

def calculateSumOfDigits(n: int)-> int:
    sum = 0
    num = n
    while num != 0:
        rem = num % 10
        sum += rem
        num = num // 10
    return sum

def calculateProductOfDigits(n: int)-> int:
    product = 1
    num = n
    while num != 0:
        rem = num % 10
        product = product * rem
        num = num // 10
    return product

n = int(input("Enter the number: "))
print(subtractProductAndSum(n=n))
