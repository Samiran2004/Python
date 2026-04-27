class BetterApproachSolution:
    def closest_number(self, n, m):
        q = int(n / m)

        # First possible closest number
        n1 = m * q

        # Second possible closest number
        if (n * m) > 0:
            n2 = (m * (q + 1))
        else:
            n2 = (m * (q - 1))

        # if true, then n1 is the required closest number
        if abs(n - n1) < abs(n - n2):
            return n1
        return n2