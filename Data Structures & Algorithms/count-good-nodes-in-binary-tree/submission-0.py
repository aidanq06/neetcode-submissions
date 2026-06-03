# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # essentially the node is always going to be a good node
        # O(n) time and O(n) space so im thinking we'll run either dfs
        # or bfs. in this situation dfs is more natural since we need to carry information 
        # throughout the nodes.


        self.goodCount = 0
        

        # first thought is that inorder dfs goes from 3, 1, 2, 1, 1, 5

        def dfs(root, largestValue):
            if not root:
                return

            if root.val >= largestValue:
                self.goodCount+=1

            largestValue = max(largestValue, root.val)
            

            dfs(root.left, largestValue)
            dfs(root.right, largestValue)



        dfs(root, root.val)
        return self.goodCount