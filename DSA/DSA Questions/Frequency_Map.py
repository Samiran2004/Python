def calculate_frequency(arr):
    frequency = dict()

    for i in range(0, len(arr)):
        if arr[i] in frequency:
            frequency[arr[i]] += 1
        else:
            frequency[arr[i]] = 1

    return frequency

size = int(input("Enter the size of the array: "))
arr = []
for i in range(0, size):
    data = int(input("Enter data: "))
    arr.append(data)
print(arr)
print(calculate_frequency(arr=arr))
