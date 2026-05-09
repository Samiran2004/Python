from BruteForce import BruteForceSolution
from BetterApproach import BetterApproachSolution

size = int(input("Enter the size of the array: "))

prices = []

for _ in range(size):
    data = int(input("Enter the price: "))
    prices.append(data)

print(f"Original price: {prices}")

print(f"Max Profit: {BruteForceSolution().maxProfit(prices)}")
print(f"Max Profit: {BetterApproachSolution().maxProfit(prices)}")