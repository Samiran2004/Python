def sumOfMultiples(n: int)-> int:
    resultSum = 0
    if n <= 1:
        return resultSum
    for i in range(1, n+1):
        if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
            resultSum += i
    return resultSum

n = int(input("Enter the value of n: "))
print(sumOfMultiples(n=n))
