from BruteForce import BruteForceSolution

arr = []
size = int(input("Enter the size of the array: "))
for _ in range(size):
    data = int(input("Enter the data of the array: "))
    arr.append(data)

result = BruteForceSolution()
print(result.threeSum(arr=arr))