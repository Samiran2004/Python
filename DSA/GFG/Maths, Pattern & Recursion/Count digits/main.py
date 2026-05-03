from UsingIterativeSolution import UsingIterativeSolutionMethod
from UsingRecursiveApproach import RecursiveApproachSolution

n: int = int(input("Enter the number: "))

print(UsingIterativeSolutionMethod().countDigit(n))

print(RecursiveApproachSolution().countDigit(n))