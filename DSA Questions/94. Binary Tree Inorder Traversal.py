from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root: Optional[TreeNode])-> List[int]:
    res = []

    def inorder(root: Optional[TreeNode]):
        if not root:
            return
        inorder(root=root.left)
        res.append(root.val)
        inorder(root=root.right)
    inorder(root=root)
    return res

root = TreeNode(val=1)
root.left = TreeNode(val=2)
root.left.left = TreeNode(val=4)
root.left.right = TreeNode(val=5)
root.left.right.left = TreeNode(val=6)
root.left.right.right = TreeNode(val=7)

root.right = TreeNode(val=3)
root.right.right = TreeNode(val=8)
root.right.right.left = TreeNode(val=9)

arr = inorderTraversal(root=root)
print(arr)
