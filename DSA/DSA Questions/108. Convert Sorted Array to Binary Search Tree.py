from typing import Optional, List

class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.leftNode: Optional[TreeNode] = None
        self.rightNode: Optional[TreeNode] = None

class Tree:
    def __init__(self, data) -> None:
        self.rootNode = TreeNode(data=data)

    def insertLeft(self, parentNode, data):
        if parentNode.leftNode is None:
            parentNode.leftNode = TreeNode(data=data)
        else:
            raise Exception("Left Child Already Exists...")
        return parentNode.leftNode

    def insertRight(self, parentNode, data):
        if parentNode.rightNode is None:
            parentNode.rightNode = TreeNode(data=data)
        else:
            raise Exception("Right Child Already Exists...")
        return parentNode.rightNode

    def print_tree(self):
        def _inorder(root):
            if root:
                _inorder(root=root.leftNode)
                print(root.data, end=' ')
                _inorder(root=root.rightNode)
        _inorder(self.rootNode)
        print()

def sortedArrayToBST(nums: List[int])-> Optional[TreeNode]:
    if not nums:
        return None
    size = len(nums)
    mid = (size - 1) // 2
    root = TreeNode(data=mid)
    root.leftNode = sortedArrayToBST(nums=nums[:mid])
    root.rightNode = sortedArrayToBST(nums=nums[mid+1:])
    return root


arr = []
size = int(input("Enter the size of the array: "))
for i in range(0, size):
    data = int(input("Enter the data: "))
    arr.append(data)

root = sortedArrayToBST(nums=arr)
tree = Tree(root)
tree.print_tree()

