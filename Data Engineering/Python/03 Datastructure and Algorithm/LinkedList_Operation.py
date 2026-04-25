from LinkedList import LinkedList

l1 = LinkedList()

size = int(input("Enter how much data you want to add: "))

for _ in range(size):
    data = int(input("Enter data: "))
    l1.append(data=data)

l1.display()

data = int(input("Enter the data to add first: "))
l1.addFirst(data=data)
l1.display()

data = int(input("Enter the data to add last: "))
l1.addLast(data=data)
l1.display()