# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        #To calculate heights of tree
        def height(curr):
            if not curr:
                return 0
            return 1 + max(height(curr.left), height(curr.right))
        
        heightLeftTree = height(root.left)
        heightRightTree = height(root.right)

        return abs(heightLeftTree - heightRightTree) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
