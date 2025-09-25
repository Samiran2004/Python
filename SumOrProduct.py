def sumOrProduct(n, q):
    if q == 1:
        result = 0
        for i in range(1, n+1):
            result += i
        
        return result
    elif q == 2:
        result = 1
        for i in range(1, n+1):
            result = result * i
        return result
    else:
        print("Error...")

number = int(input("Enter the number: "))
q = int(input("Enter the value of q: "))

print(sumOrProduct(number, q))