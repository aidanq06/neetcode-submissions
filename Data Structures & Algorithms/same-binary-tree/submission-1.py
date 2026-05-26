# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        tree1 = []
        tree2 = []

        def dfs1(root):
            if not root:
                tree1.append(None)
                return

            tree1.append(root.val)
            dfs1(root.left)
            
            dfs1(root.right)
        
        def dfs2(root):
            if not root:
                tree2.append(None)
                return

            tree2.append(root.val)
            dfs2(root.left)
            dfs2(root.right)
            
        
        dfs1(p)
        dfs2(q)

        print(tree1,tree2)
        
        return tree1 == tree2
        