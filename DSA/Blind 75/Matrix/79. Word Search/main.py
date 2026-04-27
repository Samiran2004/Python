from BruteForce import BruteForceSolution

matrix = []
row: int = int(input("Enter the size of the row: "))
column: int = int(input("Enter the size of the column: "))

for i in range(row):
    elm = []
    for j in range(column):
        data = str(input(f"Enter [{i}] [{j}]: "))
        elm.append(data)
    matrix.append(elm)

print("Original Matrix: ")
for r in matrix:
    print(r)