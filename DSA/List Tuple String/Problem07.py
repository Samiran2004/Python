def maxProfit(prices):
    profit = 0
    n = len(prices)

    for i in range(n-1):
        if prices[i+1] > prices[i]:
            profit += prices[i+1] - prices[i]

    return profit

size = int(input("Enter the size of the array: "))
arr = []
for i in range(size):
    data = int(input("Enter data: "))
    arr.append(data)
