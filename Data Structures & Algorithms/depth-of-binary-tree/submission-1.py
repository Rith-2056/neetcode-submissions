# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     if not root:
    #         return 0
    #     return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
    def maxDepth(self, root, height=1):
        if not root:
            return 0
        if not root.left and not root.right:
            return height
        if not root.right:
            return self.maxDepth(root.left, height + 1)
        if not root.left:
            return self.maxDepth(root.right, height+1)
        left = self.maxDepth(root.left, height + 1)
        right = self.maxDepth(root.right, height + 1)        
        return max(left, right)
        
        