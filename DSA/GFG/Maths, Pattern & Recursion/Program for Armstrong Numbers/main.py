from BruteForce import BruteForceSolution
from BetterApproach import BetterApproachSolution

n: int = int(input("Enter the number to check: "))

print(BruteForceSolution().armstrongNumber(n))

print(BetterApproachSolution().armstrongNumber(n))