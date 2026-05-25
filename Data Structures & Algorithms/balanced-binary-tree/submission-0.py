# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True

        def dfs(root, number=None):
            if not root: return [True,0] # booleans and the height of the true 

            left = dfs(root.left) # we want to calculate a boolean and height with this 
            right = dfs(root.right)

            balanced = (abs(left[1]-right[1])<=1) and left[0] and right[0] # we need to check if the absolute value of the left 
            # height minus the right height is less than or equal to 1. if more than 1 than its height is too
            # big, aka balanced will return False
            # additionally, if the old 

            return [balanced, 1+max(left[1],right[1])]

        return dfs(root)[0]
