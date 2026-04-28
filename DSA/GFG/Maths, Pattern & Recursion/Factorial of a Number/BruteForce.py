class BruteForceSolution:
    def factorial(self, n):
        ans = 1
        i = 2

        while i<=n:
            ans *= i
            i += 1
        return ans