from typing import Optional

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next: Optional['Node'] = None

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

    def print_list(self):
        currNode = self.head
        while currNode is not None:
            print(currNode.data, end=" ")
            currNode = currNode.next

    def find_middle(self):
        slowPtr = self.head
        fastPtr = self.head
        if self.head is None:
            return
        while fastPtr.next is not None and fastPtr.next.next is not None:
            if slowPtr is not None:
                slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next
        return slowPtr.data

list = LinkedList(1)
list.insert(2)
list.insert(3)
list.insert(4)
list.insert(5)
list.insert(6)
list.insert(7)
list.print_list()
print(list.find_middle())
