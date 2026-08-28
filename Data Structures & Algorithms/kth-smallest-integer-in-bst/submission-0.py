# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#BFS to store all elements in the array
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        visited = []
        q = collections.deque([root])
        while q:
            node = q.popleft()
            if node:
                visited.append(node.val)
                q.append(node.left)
                q.append(node.right)
        visited.sort()
        return visited[k-1]
