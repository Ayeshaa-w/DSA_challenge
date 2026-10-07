# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        def dfs(node):
            left,right=float('inf'),float('inf')
            if not node:
                return 0
            if not node.left:
                right=dfs(node.right)
            elif not node.right:
                left=dfs(node.left)
            else:
                left=dfs(node.left)
                right=dfs(node.right)
            return 1+min(left,right)
        return dfs(root)