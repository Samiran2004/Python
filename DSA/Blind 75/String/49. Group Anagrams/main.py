from BruteForce import BruteForceSolution
from BetterApproach import BetterApproachSolution

arr = []
size = int(input("Enter the size of the array: "))

for _ in range(size):
    data = str(input("Enter the data: "))
    arr.append(data)

result = BruteForceSolution()
print(result.groupAnagrams(strs=arr))

result = BetterApproachSolution()
print(result.groupAnagrams(strs=arr))