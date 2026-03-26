from typing import List
from BruteForce import SolutionBruteForce
from BetterApproach import SolutionBetterApproach


arr: List[int] = []
size: int = int(input("Enter the size of the array: "))

for _ in range(size):
    data: int = int(input("Enter data: "))
    arr.append(data)

solution = SolutionBruteForce()
print(solution.maxProfit(prices=arr))

solution = SolutionBetterApproach()
print(solution.maxProfit(prices=arr))