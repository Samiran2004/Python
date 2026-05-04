class BetterApproachSolution:
    def largestPrimeFactor(self, n):
        max_prime = -1
        i = 2

        while i * i <= n:
            while n % i == 0:
                max_prime = i
                n = n // i
            i += 1

        if n > 1:
            max_prime = n
        return max_prime