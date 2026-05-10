class BruteForceSolution:
    def maxProfit(self, prices):
        def maxProfitRes(price, start, end):
            res = 0
            for i in range(start, end):
                for j in range(i + 1, end + 1):
                    if price[j] > price[i]:
                        curr = (price[j] - price[i] + maxProfitRes(price, start, i - 1) + maxProfitRes(price, j + 1, end))
                        res = max(res, curr)
            return res

        return maxProfitRes(prices, 0, len(prices) - 1)