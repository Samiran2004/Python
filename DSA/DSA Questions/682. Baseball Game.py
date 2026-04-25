from typing import List
def calPoints(operations: List[int])-> int:
    record = []
    for i in operations:
        try:
            if type(int(i)) == int:
                record = record+[int(i)]
        except:
            if i == 'D':
                record = record + [record[-1]*2]
            elif i == 'C':
                record.pop(-1)
            elif i == '+':
                record = record + [record[-1] + record[-2]]
    return sum(record)


arr = list()
size = int(input("Enter the size of the array: "))
for i in range(0, size):
    data = int(input("Enter the data: "))
    arr.append(data)
