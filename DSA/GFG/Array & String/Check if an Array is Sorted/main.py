from BruteForce import BruteForceSolution
from BetterApproach import BetterApproachSolution
from UsingBuiltInMethod import UsingBuiltInMethodSolution

size = int(input("Enter the size of the array: "))

arr = []

for _ in range(size):
    data = int(input("Enter data: "))
    arr.append(data)

print(BruteForceSolution().isSorted(arr))

print(BetterApproachSolution().isSorted(arr))

print(UsingBuiltInMethodSolution().isSorted(arr))