from BruteForce import BruteForceSolution
from BetterApproach import BetterApproachSolution

s: str = str(input("Enter the string: "))
t: str = str(input("Enter the value of t: "))

result = BruteForceSolution()
print(result.minWindow(s=s, t=t))

result = BetterApproachSolution()
print(result.minWindow(s=s, t=t))