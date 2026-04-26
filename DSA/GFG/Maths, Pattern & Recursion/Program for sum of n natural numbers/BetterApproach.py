class BetterApproachSolution:
    def sumOfNaturals(self, n: int):
        if n == 1:
            return 1
        return n + self.sumOfNaturals(n - 1)