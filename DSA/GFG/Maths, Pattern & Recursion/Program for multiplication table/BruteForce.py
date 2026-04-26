class BruteForceSolution:
    def printTable(self, n: int):
        for i in range(1, 11):
            print("%d * %d = %d" % (n, i, n * i))