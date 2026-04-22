from BruteForce import BruteForceSolution
from BetterApproach import BetterApproachSolution

n = int(input("Enter the number: "))

result = BruteForceSolution()
print(f"{n} is a palindrome: {result.isPalindrome(x=n)}")

result = BetterApproachSolution()
print(f"{n} is a palindrome: {result.isPalindrome(x=n)}")