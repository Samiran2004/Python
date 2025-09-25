def maxProfit(prices):
    min_price = prices[0]
    profit = 0

    for i in range(1, len(prices)):
        curr_profit = prices[i] - min_price
        if curr_profit > profit:
            profit = curr_profit
        min_price = min(min_price, prices[i])
    return profit

size = int(input("Enter the size of the array: "))
arr = []

for i in range(0, size):
    data = int(input("Enter data: "))
    arr.append(data)
