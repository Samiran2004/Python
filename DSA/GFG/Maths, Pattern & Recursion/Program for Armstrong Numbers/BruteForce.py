class BruteForceSolution:
    def armstrongNumber(self, n: int):
        # Function to calculate x raised to the power y
        def power(x, y):
            if y == 0:
                return 1
            if y % 2 == 0:
                return power(x, y // 2) * power(x, y // 2)
            return x * power(x, y // 2) * power(x, y // 2)

        # Function to count number of digits in n
        def order(n):
            t = 0
            while n:
                t += 1
                n = n // 10
            return t
        x = order(n)
        temp = n
        sum_ = 0

        while temp:
            rem = temp % 10
            sum_ += power(rem, x)
            temp = temp // 10
        return sum_ == n