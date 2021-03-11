# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        self.leveller(root, 0, result)
        return result
    
    def leveller(self, root, curr_level, result):
        #result is an empty list
        #counter is required i guess
        if not root:
            return [result]
        if root is not None:
            # print(curr_level)
            # print(result)
            if curr_level == len(result):
                result.append([root.val])
            else:
                result[curr_level].append(root.val)
                
            temp_level = curr_level + 1
            if root.left is not None:
                self.leveller(root.left, temp_level, result)
            if root.right is not None:
                self.leveller(root.right, temp_level, result)
                
        return result
