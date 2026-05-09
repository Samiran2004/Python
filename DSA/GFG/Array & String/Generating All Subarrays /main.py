from BruteForce import BruteForceSolution
from BetterApproach import BetterApproachSolution
from OptimalApproach import OptimalApproachSolution

size = int(input("Enter the size of the array: "))
arr = []

for _ in range(size):
    data = int(input("Enter the data: "))
    arr.append(data)

print(BruteForceSolution().getSubArrays(arr))

print(BetterApproachSolution().getSubArrays(arr))

print(OptimalApproachSolution().getSubArrays(arr))