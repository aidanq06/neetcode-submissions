# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # first thought is to
        # recursively run a form of dfs probably probably inorder. 
        # we then add all the numbers to a list
        # we sort that list
        # then get the ith value in that list and return 

        self.numList = []

        def dfs(root):
            if not root:
                return

            dfs(root.left)
            self.numList.append(root.val)
            dfs(root.right)
        
        dfs(root)
        return self.numList[k-1]