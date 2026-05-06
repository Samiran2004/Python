import copy

from BruteForce import BruteForceSolution
from BetterApproach import BetterApproachSolution

size = int(input("Enter the size of the array: "))
arr = []

for _ in range(size):
    data = int(input("Enter data: "))
    arr.append(data)

d = int(input("Enter the rotation value: "))

temp1 = copy.deepcopy(arr)
BruteForceSolution().rotateArr(temp1, d)
print(temp1)

temp1 = copy.deepcopy(arr)
BetterApproachSolution().rotateArr(temp1, d)
print(temp1)