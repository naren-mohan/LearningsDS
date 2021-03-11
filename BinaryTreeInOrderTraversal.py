# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        self.traverse(root, result)
        return result
    
    def traverse(self, root, result):
        if not root:
            return result
        if root.left is None and root.right is None:
            result.append(root.val)
            return result
        if root is not None:
            if root.left is not None:
                self.traverse(root.left, result)
            result.append(root.val) #should I 
            if root.right is not None:
                self.traverse(root.right, result)
            #result.append(root.val)
        return result
