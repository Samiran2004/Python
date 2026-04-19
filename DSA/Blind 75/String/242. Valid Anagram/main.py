from BruteForce import BruteForceSolution
from BetterApproach import BetterApproachSolution

s: str = str(input("Enter the first string: "))
t: str = str(input("Enter the second string: "))

result = BruteForceSolution()
print(result.isAnagram(s=s, t=t))

result = BetterApproachSolution()
print(result.isAnagram(s=s, t=t))