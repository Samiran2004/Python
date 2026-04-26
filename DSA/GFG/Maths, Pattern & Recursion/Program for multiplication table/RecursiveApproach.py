class RecursiveApproachSolution:
    def printTable(self, n, i = 1):
        if i == 11:
            return
        print(n, "*", i, "=", n*i)
        i += 1
        self.printTable(n=n, i=i)