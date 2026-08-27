# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def findMin(root): 
            curr = root
            while curr and curr.left: 
                curr = curr.left
            return curr.val
        if not root: 
            return None
        if root.val == key: 
            if root.left is None and root.right is None: 
                return None
            elif root.left is None or root.right is None: 
                root = root.left if root.left else root.right
            else: 
                minNode = findMin(root.right)
                root.val = minNode
                root.right = self.deleteNode(root.right, minNode)
        if key > root.val: 
            root.right = self.deleteNode(root.right, key)
        else: 
            root.left = self.deleteNode(root.left, key)
        return root