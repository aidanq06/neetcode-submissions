# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # we essentially want to keep the max() of each height. 
        # to keep it O(n) we'll only cycle through the entire loop once
        # we'll use DFS

        def dfs(root):
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            return 1+max(left, right)
        
        return dfs(root)