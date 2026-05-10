from BruteForce import BruteForceSolution
from BetterApproach import BetterApproachSolution

prices = []
size = int(input("Enter the size of the prices array: "))

for _ in range(size):
    data = int(input("Enter price: "))
    prices.append(data)

print(f"Prices: {prices}")

print(BruteForceSolution().maxProfit(prices))

print(BetterApproachSolution().maxProfit(prices))