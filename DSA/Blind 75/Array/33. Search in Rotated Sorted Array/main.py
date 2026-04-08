from BruteForce import BruteForceSolution
from OptimalApproach import OptimalApproachSolution

arr = []
size = int(input("Enter the size of the array: "))
for _ in range(size):
    data = int(input("Enter the data: "))
    arr.append(data)

target: int = int(input("Enter the value of target: "))

result = BruteForceSolution()
print(result.search(nums=arr, target=target))

result = OptimalApproachSolution()
print(result.search(nums=arr, target=target))