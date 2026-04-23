from BruteForce import BruteForceSolution
from BetterApproach import BetterApproachSolution

s: str = str(input("Enter the string: "))

result = BruteForceSolution()
print(result.longestPalindrome(s=s))

result = BetterApproachSolution()
print(result.longestPalindrome(s=s))