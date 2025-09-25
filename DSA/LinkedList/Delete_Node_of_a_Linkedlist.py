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

        currNode = self.head
        while currNode.next != None:
            currNode = currNode.next

        currNode.next = newNode

    def display(self):
        if self.head == None:
            print("List is empty...")
            return
        currNode = self.head
        while currNode != None:
            print(currNode.data, end=" ")
            currNode = currNode.next
        print()

    def delete_node(self, value):
        if self.head is None:
            print("List is empty...")
            return

        currNode = self.head
        while currNode.next is not None and currNode.next.data != value:
            currNode = currNode.next
        currNode.next = currNode.next.next
        return self.head

list = LinkedList(1)
list.insert(2)
list.insert(3)
list.insert(4)
list.insert(5)
list.display()
list.delete_node(4)
list.display()
list.delete_node(5)
list.display()
