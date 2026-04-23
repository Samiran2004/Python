from BruteForce import BruteForceSolution
from BetterApproach import BetterApproachSolution

s: str = str(input("Enter the string: "))

result = BruteForceSolution()
print(result.countSubstrings(s=s))

result = BetterApproachSolution()
print(result.countSubstrings(s=s))