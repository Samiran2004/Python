from BruteForce import BruteForceSolution
from BetterApproach import BetterApproachSolution

n = int(input("Enter the number: "))

result = BruteForceSolution()
print(result.hammingWeight(n=n))

result = BetterApproachSolution()
print(result.hammingWeight(n=n))