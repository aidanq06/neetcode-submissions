# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        # first thought
        # essentially we're trying to find the longest "chain" in the binary tree, running edge to edge.
        # the chain is the longest number of nodes connected without including the same node twice.

        # im imaging 
        #. diameter = 2
        #    1
        #     2
        #    3 4
        #   5   
        #. 6     

        # inorder dfs will start at the bottom
        # preorder dfs will start counting at the top

        # second thought, we can check for the diameter at each node by checking the height of the left and the right of each node.
        # however, using dfs, we can turn it down from O(n^2) time complexity (checking the possibilities of EACH node) to O(n), which
        # calculates the height going up from each "leaf" node. 

        # lets think all the way at the bottom, at 9. it checks the height of 9, which is one, checks the height of 8 which is one.
        # the maxDiameter is then updated to include BOTH of these heights. THEN that specific node will return "max(left,right)"  which is 1.
        # the maxDiameter would be 2 for the node that is 5.

        self.maxDiameter = 0

        def dfs(root):
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            self.maxDiameter = max(self.maxDiameter, left+right)
            return 1+ max(left,right)

        dfs(root)
        return self.maxDiameter

        """
        stack = list()
        def dfs(root, stack):
            if not root:
                return 0
            
            current = max(dfs(root.left), dfs(root.right))
            if root.val not in stack:
                stack.append(root.val)
                return current+1
            elif root.val in stack and stack[-2] != root.val: # can't be the second to last
                stack.append(root.val)
                return current+1
            else
        """
                
            
            