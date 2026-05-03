from BruteForce import BruteForceSolution

arr = []

row = int(input("Enter the size of the row: "))
column = int(input("Enter the size of the column: "))

for i in range(row):
    col_arr = []
    for j in range(column):
        data = int(input(f"Enter {i}, {j} data of the array: "))
        col_arr.append(data)
    arr.append(col_arr)

new_intervals = []
size = int(input("Enter the size of the new interval: "))
for i in range(size):
    data = int(input("Enter the data for new interval: "))
    new_intervals.append(data)
print(f"New interval array is: {new_intervals}")

print("Original Array: ")
print(arr)

result = BruteForceSolution().insert(intervals=arr, newInterval=new_intervals)
print(result)