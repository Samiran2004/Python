from BruteForce import BruteForceSolution
from BetterApproach import BetterApproachSolution

num: int = int(input("Enter the number: "))

result = BruteForceSolution().factorial(num)
print(result)

result = BetterApproachSolution().factorial(num)
print(result)