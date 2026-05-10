from BruteForceApproach import BruteForceApproachSolution
from BetterApproach import BetterApproachSolution
from OptimizeApproach import OptimizeApproachSolution

arr = []
size = int(input("Enter the size of the array: "))

for _ in range(size):
    data = int(input("Enter the data of the array: "))
    arr.append(data)

print(f"Array: {arr}")

print(BruteForceApproachSolution().leaders(arr))
print(BetterApproachSolution().leaders(arr))
print(OptimizeApproachSolution().leaders(arr))