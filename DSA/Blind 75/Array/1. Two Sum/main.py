from typing import List
from BruteForce import Solution_Brute_Force
from BetterApproach import SolutionBetterApproach

arr: List[int] = []
size: int = int(input("Enter the size of the array: "))

for _ in range(size):
    data: int = int(input("Enter the data: "))
    arr.append(data)

target: int = int(input("Enter the value of the target: "))

solution = Solution_Brute_Force()
print(solution.twoSum(arr=arr, target=target))

solution = SolutionBetterApproach()
print(solution.twoSum(arr=arr, target=target))