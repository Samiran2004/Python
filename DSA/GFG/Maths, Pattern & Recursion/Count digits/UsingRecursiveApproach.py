class RecursiveApproachSolution:
    def countDigit(self, n: int):
        if n // 10 == 0:
            return 1
        return 1 + self.countDigit(n // 10)