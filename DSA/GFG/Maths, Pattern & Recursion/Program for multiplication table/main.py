from BruteForce import BruteForceSolution
from RecursiveApproach import RecursiveApproachSolution

n: int = int(input("Enter the number: "))

result = BruteForceSolution()
print(result.printTable(n=n))

result = RecursiveApproachSolution()
print(result.printTable(n=n))