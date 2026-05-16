from BruteForceApproach import BruteForceApproachSolution
from BetterApproach import BetterApproachSolution

size = int(input("Enter the size of the array: "))
arr = []

for _ in range(size):
    data = int(input("Enter the data: "))
    arr.append(data)

print(BruteForceApproachSolution().findMajority(arr))
print(BetterApproachSolution().findMajority(arr))