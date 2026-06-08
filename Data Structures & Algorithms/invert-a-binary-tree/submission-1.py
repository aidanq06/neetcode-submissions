# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # so when we're thinking about this question we want to switch the left and right 
        
        def dfs(root):
            if not root:
                return

            right = dfs(root.right)
            left = dfs(root.left)

            root.left = right
            root.right = left

            return root

        return dfs(root)