# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#O(n) solution -> beautiful implementation
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if root is None:
                return [True, 0]
            left = dfs(root.left)
            right = dfs(root.right)
            #Needs to be a boolean value -> two conditions: 
            #Difference between the left and right subtrees is 1 and at any point if there is a False
            balanced = left[0] and right[0] and (abs(left[1] - right[1]) <= 1)
            return [balanced, 1 + max(left[1], right[1])]
        return dfs(root)[0]
