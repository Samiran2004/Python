import math


class BetterApproachSolution:
    def getDivisors(self, n):
        divisor = []

        for i in range(1, int(math.sqrt(n)) + 1):
            if n % i == 0:
                if n // i == i:
                    divisor.append(i)
                else:
                    divisor.append(i)
                    divisor.append(n // i)

        return divisor