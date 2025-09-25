from typing import Optional

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next: Optional[Node] = None

class LinkedList:
    head = None
    def __init__(self, data) -> None:
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

    def calculateSize(self):
        length = 0
        currNode = self.head
        while currNode is not None:
            length += 1
            currNode = currNode.next
        return length

    def delete_from_end(self, pos):
        length = self.calculateSize()
        currNode = self.head
        currPos = 0
        while currPos != (length - pos +1) and currNode is not None:
            currPos += 1
            currNode = currNode.next
        currNode.next = currNode.next.next

list = LinkedList(1)
list.insert(2)
list.insert(3)
list.insert(4)
list.insert(5)
list.display()
list.delete_from_end(3)
list.display()
