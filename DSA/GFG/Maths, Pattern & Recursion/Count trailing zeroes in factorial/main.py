from BruteForce import BruteForceSolution
from BetterApproach import BetterApproachSolution

n: int = int(input("Enter the number: "))

print(BruteForceSolution().trailingZeroes(n))

print(BetterApproachSolution().trailingZeroes(n))