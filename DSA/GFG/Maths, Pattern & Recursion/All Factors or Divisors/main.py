from BruteForce import BruteForceSolution
from BetterApproach import BetterApproachSolution

n: int = int(input("Enter the number: "))

print(BruteForceSolution().getDivisors(n))

print(BetterApproachSolution().getDivisors(n))