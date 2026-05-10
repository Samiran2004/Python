class BetterApproachSolution:
    def maxProfit(self, prices):
        res = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                res += prices[i] - prices[i - 1]
        return res