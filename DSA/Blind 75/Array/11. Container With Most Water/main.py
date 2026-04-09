from BruteForce import BruteForceSolution
from BetterApproach import BetterApproachSolution

arr = []
size = int(input("Enter the size of the array: "))

for _ in range(size):
    data = int(input("Enter data: "))
    arr.append(data)

result = BruteForceSolution()
print(result.maxArea(height=arr))

result = BetterApproachSolution()
print(result.maxArea(height=arr))