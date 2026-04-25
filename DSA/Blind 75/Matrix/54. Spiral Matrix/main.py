from BruteForce import BruteForceSolution

row = int(input("Enter the size of the row of the matrix: "))
column = int(input("Enter the size of the column of the matrix: "))
matrix = []

for i in range(row):
    current_row = []
    print(f"Enter elements for row {i + 1}:")

    for j in range(column):
        val = int(input(f"Enter element [{i}][{j}]: "))
        current_row.append(val)

    matrix.append(current_row)

print("Original Matrix")
for r in matrix:
    print(r)

result = BruteForceSolution().spiralOrder(matrix)

print(result)