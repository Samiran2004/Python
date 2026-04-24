import copy

from BruteForce import BruteForceSolution
from BetterApproach import BetterApproachSolution

matrix = []

row = int(input("Enter the number of rows: "))
column = int(input("Enter the number of columns: "))

for i in range(row):
    current_row = []
    print(f"Enter elements for row {i+1}:")
    
    for j in range(column):
        val = int(input(f"Enter element [{i}][{j}]: "))
        current_row.append(val)
    
    matrix.append(current_row)

print("Matrix is:")
for r in matrix:
    print(r)
    
matrix_bruteforce = copy.deepcopy(matrix)
result = BruteForceSolution()
result.setZeroes(matrix=matrix_bruteforce)
print("Matrix is after Bruteforce solution: ")
for r in matrix_bruteforce:
    print(r)
    

matrix_better = copy.deepcopy(matrix)
result = BetterApproachSolution()
result.setZeroes(matrix=matrix_better)
print("Matrix is after Betterapproach solution: ")
for r in matrix_better:
    print(r)