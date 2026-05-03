class BetterApproachSolution:
    def armstrongNumber(self, n: int):
        number = str(n)

        digits = len(number)

        output = 0

        for i in number:
            output += int(i) ** digits

        return output == n