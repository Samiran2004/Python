from BruteForceApproach import BruteForceApproachSolution
from BetterApproach import BetterApproachSolution

s: str = str(input("Enter the string: "))

print(BruteForceApproachSolution().checkPangram(s))

print(BetterApproachSolution().checkPangram(s))