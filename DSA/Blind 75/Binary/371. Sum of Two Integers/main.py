from BruteForce import BruteForceSolution
from BetterApproach import BetterApproachSolution

a = int(input("Enter the first value: "))
b = int(input("Enter the second value: "))

result = BruteForceSolution()
print(result.getSum(a=a, b=b))

result = BetterApproachSolution()
print(result.getSum(a=a, b=b))