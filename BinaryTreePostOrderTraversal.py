# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        self.traverse(root, result)
        return result
    
    def traverse(self, root, result):
        if not root:
            return result
        if root.left is None and root.right is None:
            result.append(root.val)
        elif root is not None:
            if root.left is not None:
                self.traverse(root.left, result)
            if root.right is not None:
                self.traverse(root.right, result)
            result.append(root.val)
        return result
