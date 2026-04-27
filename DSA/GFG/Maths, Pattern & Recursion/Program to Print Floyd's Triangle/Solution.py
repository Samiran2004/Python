def printFloydTriangle(n):
    val = 1
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(val, end=" ")
            val += 1
        print()