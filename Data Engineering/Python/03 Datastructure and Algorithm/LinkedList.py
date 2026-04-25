class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0
    
    def append(self, data):
        newNode = Node(data=data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode # type: ignore
            self.tail = newNode
        self.length += 1
    
    def addFirst(self, data):
        newNode = Node(data=data)
        newNode.next = self.head # type: ignore
        self.head = newNode
        if self.tail is None:
            self.tail = newNode
        self.length += 1
    
    def addLast(self, data):
        newNode = Node(data=data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1 
    
    def addAfter(self, target, data):
        newNode = Node(data=data)
        
        if self.head is None:
            raise Exception("List is empty...")
        
        currNode = self.head
        
        while currNode is not None:
            if currNode.data == target:
                newNode.next = currNode.next
                currNode.next = newNode
                if currNode == self.tail:
                    self.tail = newNode
                self.length += 1
                return
            currNode = currNode.next
        
        raise Exception(f"Target: {target} not found in list.")
    
    def addBefore(self, target, data):
        newNode = Node(data=data)
        
        if self.head is None:
            raise Exception("List is empty...")
        
        if self.head.data == target:
            newNode.next = self.head
            self.head = newNode
            self.length += 1
            return
        
        currNode = self.head
        
        while currNode.next is not None:
            if currNode.next.data == target:
                newNode.next = currNode.next
                currNode.next = newNode
                self.length += 1
                return
            currNode = currNode.next
        
        raise Exception(f"Target: {target} is not found in list.")
    
    def display(self):
        elements = []
        currNode = self.head
        
        while currNode is not None:
            elements.append(str(currNode.data))
            currNode = currNode.next
        
        print(" -> ".join(elements) if elements else "Empty List")