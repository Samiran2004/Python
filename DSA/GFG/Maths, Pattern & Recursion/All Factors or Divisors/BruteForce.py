class BruteForceSolution:
    def getDivisors(self, n: int):
        divisor = []

        for i in range(1, n):
            if n % i == 0:
                divisor.append(i)

        return divisor