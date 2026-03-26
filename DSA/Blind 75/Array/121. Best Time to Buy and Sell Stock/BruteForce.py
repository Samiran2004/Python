from typing import List


class SolutionBruteForce:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                currProfit = prices[j] - prices[i]
                
                max_profit = max(currProfit, max_profit)
        
        return max_profit