from BruteForce import BruteForceSolution
from BetterApproach import BetterApproachSolution

n = int(input("Enter the value of n: "))
m = int(input("Enter the value of m: "))

result = BruteForceSolution().closest_number(n, m)
print(result)

result = BetterApproachSolution().closest_number(n, m)
print(result)