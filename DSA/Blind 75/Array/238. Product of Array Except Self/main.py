from BruteForce import BruteForceSolution

arr = []
size = int(input("Enter size of the array: "))

for _ in range(size):
    data = int(input("Enter data: "))
    arr.append(data)

result = BruteForceSolution()
print(result.productExceptSelf(arr=arr))