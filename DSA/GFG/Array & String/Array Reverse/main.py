import copy

from BruteForce import BruteForceSolution
from UsingTwoPointersApproach import UsingTwoPointersApproachSolution
from UsingSinglePointerApproach import UsingSinglePointerApproachSolution

size = int(input("Enter the size of the array: "))
arr = []

for _ in range(size):
    data = int(input("Enter data: "))
    arr.append(data)

print(f"Original Array: {arr}")

temp1 = copy.deepcopy(arr)
BruteForceSolution().reverseArray(temp1)
print(f"Reversed Array [Using Bruteforce Approach]: {temp1}")

temp1 = copy.deepcopy(arr)
UsingTwoPointersApproachSolution().reverseArray(temp1)
print(f"Reversed Array [Using Two Pointers Approach]: {temp1}")

temp1 = copy.deepcopy(arr)
UsingSinglePointerApproachSolution().reverseArray(temp1)
print(f"Reversed Array [Using Two Pointers Approach]: {temp1}")