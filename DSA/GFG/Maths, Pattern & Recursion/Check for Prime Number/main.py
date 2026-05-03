from UsingNaiveApproach import UsingNativeApproachSolution
from BetterApproach import BetterApproachSolution

n: int = int(input("Enter the number: "))

print(UsingNativeApproachSolution().isPrime(n))
print(BetterApproachSolution().isPrime(n))