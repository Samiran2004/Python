from BruteForce import BruteForceSolution
from BetterApproach import BetterApproachSolution

s: str = str(input("Enter the string: "))
k: int = int(input("Enter the value of k: "))

result = BruteForceSolution()
print(result.characterReplacement(s=s, k=k))

result = BetterApproachSolution()
print(result.characterReplacement(s=s, k=k))