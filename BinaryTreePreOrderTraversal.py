# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=None, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
        
class Solution:
    
        
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        
        sol_list = []
        sol_list = self.traverse(root, sol_list)
        return sol_list
    
    def traverse(self, root, result):
        if not root:
            return result
        if root is not None:
            result.append(root.val)
        if root.left is not None:
            self.traverse(root.left, result)
        if root.right is not None:
            self.traverse(root.right, result)
        return result
        
