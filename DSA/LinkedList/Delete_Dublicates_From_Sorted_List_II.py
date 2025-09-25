from typing import Optional

class Node:
    def __init__(self, data):
        self.data = data
        self.next: Optional[Node] = None

class LinkedList:
    head: Optional[Node] = None

    def __init__(self, data):
        newNode = Node(data=data)
        self.head = newNode

    def insert(self, data):
        newNode = Node(data=data)

        if self.head is None:
            self.head = newNode
            return
        currNode = self.head
        while currNode.next is not None:
            currNode = currNode.next
        currNode.next = newNode

    def display(self):
        if self.head is None:
            print("List is empty...")
            return
        currNode = self.head
        while currNode is not None:
            print(currNode.data, end=" ")
            currNode = currNode.next
        print()

    def removeDuplicates(self):
        if self.head is None or self.head.next is None or self.head.next.next is None:
            print("List is empty or data is not have that much data to perform this operation...")
            return
        currNode = self.head
        while currNode is not None and currNode.next is not None and currNode.next.next is not None:
            if self.head.data == self.head.next.data:
                self.head = self.head.next.next
            if currNode.next.data == currNode.next.next.data:
                currNode.next = currNode.next.next.next
            else:
                currNode = currNode.next


list = LinkedList(1)
list.insert(1)
list.insert(2)
list.insert(2)
list.insert(3)
list.insert(4)
list.insert(4)
list.insert(5)
list.display()
list.removeDuplicates()
list.display()
