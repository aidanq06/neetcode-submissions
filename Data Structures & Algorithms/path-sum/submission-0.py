# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        # we basically want to recursively pass down the sum of each node starting from the root.
        # we want to run a dfs

        def dfs(root, sumNodes):
            if not root:
                return False
            sumNodes+=root.val
            
            left = dfs(root.left, sumNodes)    
            right = dfs(root.right, sumNodes)
            
            if not root.left and not root.right and sumNodes != targetSum:
                return False
            # not left + not right = leaf node, if itsa leaf node and the sumNodes isn't equal to the target
            # then return False
            
            elif not root.left and not root.right and sumNodes == targetSum:
                return True
            return left or right

                #1
              #1    #0
            #1

        return dfs(root, 0)