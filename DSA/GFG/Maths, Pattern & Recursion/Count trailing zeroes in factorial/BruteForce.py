from math import factorial


class BruteForceSolution:
    def trailingZeroes(self, n: int):
        fact = factorial(n)
        count = 0

        while fact % 10 == 0:
            count += 1
            fact = fact // 10
        return count