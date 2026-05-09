from Solution import Solutions

size = int(input("Enter the size of the array: "))
arr = []

for _ in range(size):
    data = int(input("Enter the data: "))
    arr.append(data)

print(f"Original Array: {arr}")

Solutions().rearrange(arr)

print(f"Rearrange array: {arr}")