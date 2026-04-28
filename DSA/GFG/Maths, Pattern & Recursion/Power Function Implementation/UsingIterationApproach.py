class UsingIterationApproachSolution:
    def power(self, b, e):
        pow = 1
        for i in range(abs(e)):
            pow = pow * b
        if e < 0:
            return 1/pow
        return pow