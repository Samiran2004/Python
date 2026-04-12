class BetterApproachSolution:
    def hammingWeight(self, n: int):
        count = 0
        while n:
            n = n & (n - 1)
            count += 1
        return count