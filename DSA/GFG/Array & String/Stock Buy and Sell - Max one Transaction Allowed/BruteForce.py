class BruteForceSolution:
    def maxProfit(self, prices):
        res = 0

        for i in range(len(prices) - 1):
            for j in range(i+1, len(prices)):
                res = max(res, prices[j] - prices[i])

        return res