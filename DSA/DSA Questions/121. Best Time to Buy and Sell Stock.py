from typing import List

def maxProfit(prices: List[int])-> int:
    min_price = prices[0]
    profit = 0
    for i in range(1, len(prices)):
        curr_profit = prices[i] - min_price
        if curr_profit > profit:
            profit = curr_profit
        min_price = min(min_price, prices[i])
    return profit

prices: list = list()
size: int = int(input("Enter the size of the prices list: "))

for _ in range(size):
    data: int = int(input("Enter the data: "))
    prices.append(data)

print(maxProfit(prices=prices))