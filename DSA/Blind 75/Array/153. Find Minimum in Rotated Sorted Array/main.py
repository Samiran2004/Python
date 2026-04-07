from BruteForce import BruteForceSolution
from OptimalApproach import OptimalApproachSolution

arr = []
size = int(input("Enter the size of the array: "))
for _ in range(size):
    data = int(input("Enter the data: "))
    arr.append(data)

result = BruteForceSolution()
print(result.findMin(arr=arr))

result = OptimalApproachSolution()
print(result.findMin(arr=arr))