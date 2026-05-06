from BruteForce import BruteForceSolution

size = int(input("Enter the size of the array: "))
arr = []
for i in range(size):
    data = int(input("Enter the data: "))
    arr.append(data)

k = int(input("Enter the value of k: "))

print(f"Original Array: {arr}")
BruteForceSolution().reverseingroups(arr,k)
print(f"Reversed Array: {arr}")