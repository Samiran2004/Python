from BruteForce import BruteForceSolution
from BetterApproach import BetterApproachSolution
from OptimalApproach import OptimalApproachSolution

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

result = BruteForceSolution()
print(result.maxSubArray(arr=arr))

result = BetterApproachSolution()
print(result.maxSubArray(arr=arr))

result = OptimalApproachSolution()
print(result.maxSubArray(arr=arr))