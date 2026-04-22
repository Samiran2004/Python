from BruteForce import BruteForceSolution
from BetterApproach import BetterApproachSolution

s: str = str(input("Enter the parentheses: "))

result = BruteForceSolution()
print(f"{s} is a valid parentheses(Brute Force): {result.isValid(s=s)}")

result = BetterApproachSolution()
print(result.isValid(s=s))