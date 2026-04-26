from BruteForce import BruteForceSolution
from BetterApproach import BetterApproachSolution
from OptimalApproach import OptimalApproachSolution

n: int = int(input("Enter the number: "))

result = BruteForceSolution()
print(result.sumOfNaturals(n=n))

result = BetterApproachSolution()
print(result.sumOfNaturals(n=n))

result = OptimalApproachSolution()
print(result.sumOfNaturals(n=n))