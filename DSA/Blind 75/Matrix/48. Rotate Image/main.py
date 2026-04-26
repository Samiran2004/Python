from BruteForce import BruteForceSolution
from BetterApproach import BetterApproachSolution

row = int(input("Enter the size of the row: "))
column = int(input("Enter the size of the column: "))
matrix = []

for i in range(row):
    elm = []
    for j in range(column):
        data = int(input(f"Enter the data of the [{i}] [{j}] number element of the matrix: "))
        elm.append(data)
    matrix.append(elm)

print("Original Matrix: ")
for r in matrix:
    print(r)

result = BruteForceSolution().rotate(matrix=matrix)

print("Rotate matrix after bruteforce solution: ")
for r in result:
    print(r)

print("Rotate matrix after better approach solution: ")
BetterApproachSolution().rotate(matrix=matrix)
for r in matrix:
    print(r)