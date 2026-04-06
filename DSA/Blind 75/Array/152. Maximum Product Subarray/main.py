from BruteForce import BruteForceSolution
from OptimalApproach import OptimalApproachSolution

arr = [2,3,-2,4]

result = BruteForceSolution()
print(result.maxProduct(arr=arr))

result = OptimalApproachSolution()
print(result.maxProduct(arr=arr))