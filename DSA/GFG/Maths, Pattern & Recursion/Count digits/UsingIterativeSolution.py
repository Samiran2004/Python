class UsingIterativeSolutionMethod:
    def countDigit(self, n: int):
        if n < 10:
            return 1
        x: int = n

        count: int = 0

        while x != 0:
            count += 1
            x = x // 10
        return count