# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        def dfs(node):
            if  not node:
                return 
            if node.val<val:
                return dfs(node.right)
            if node.val>val:
                return dfs(node.left)
            return node
        ans=dfs(root)
        return ans
            