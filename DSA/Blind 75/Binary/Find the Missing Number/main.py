from BruteForce import BruteForceSolution
from BetterApproach import BetterApproachSolution
from OptimalApproach import OptimalApproachSolution

arr = []
size = int(input("Enter the size of the array: "))
for _ in range(size):
    data = int(input("Enter the data: "))
    arr.append(data)

result = BruteForceSolution()
print(result.missingNum(arr=arr))

result = BetterApproachSolution()
print(result.missingNum(arr=arr))

result = OptimalApproachSolution()
print(result.missingNum(arr=arr))