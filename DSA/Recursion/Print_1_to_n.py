num = int(input("Enter the end number: "))

i = 1

def printNumber(i, n):
    # Base case...
    if i > n:
        return

    # Recursive case...
    print(i, end=" ")
    printNumber(i+1, n)


printNumber(1, num)
