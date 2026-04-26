from BruteForce import BruteForceSolution
from BetterApproach import BetterApproachSolution

n: int = int(input("Enter the number: "))

result = BruteForceSolution()
print(result.isEven(n=n))

result = BetterApproachSolution()
print(result.isEven(n=n))