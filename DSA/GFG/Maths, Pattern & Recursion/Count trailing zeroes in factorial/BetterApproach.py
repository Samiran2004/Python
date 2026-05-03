class BetterApproachSolution:
    def trailingZeroes(self, n):
        if n < 0:
            return -1

        count = 0

        while n >= 5:
            n = n // 5
            count += n
        return count